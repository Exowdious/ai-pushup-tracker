import { useState, useEffect, useRef } from 'react'
import axios from 'axios'
import './App.css'
import StatCard from './components/StatCard'
import CameraFeed from './components/CameraFeed'
import Controls from './components/Controls'
import StartupPage from './components/StartupPage'

const API_URL = 'http://localhost:8000'

function App() {
  const [showStartup, setShowStartup] = useState(true)
  const [isRunning, setIsRunning] = useState(false)
  const [stats, setStats] = useState({
    total_reps: 0,
    form_state: 'Neutral',
    stage: 'Up'
  })
  const wsRef = useRef(null)

  const handleStartApp = () => {
    setShowStartup(false)
  }

  // Add/remove body class for scrolling when startup page is shown
  useEffect(() => {
    if (showStartup) {
      document.body.style.overflow = 'auto'
      document.documentElement.style.overflow = 'auto'
    } else {
      document.body.style.overflow = 'hidden'
      document.documentElement.style.overflow = 'hidden'
    }
  }, [showStartup])

  // WebSocket connection for real-time stats
  useEffect(() => {
    if (isRunning) {
      wsRef.current = new WebSocket('ws://localhost:8000/ws/stats')
      
      wsRef.current.onmessage = (event) => {
        const data = JSON.parse(event.data)
        setStats(data)
      }

      wsRef.current.onerror = (error) => {
        console.error('WebSocket error:', error)
      }

      return () => {
        if (wsRef.current) {
          wsRef.current.close()
        }
      }
    }
  }, [isRunning])

  const handleStart = async () => {
    try {
      await axios.post(`${API_URL}/camera/start`)
      setIsRunning(true)
    } catch (error) {
      console.error('Failed to start camera:', error)
      alert('Failed to start camera. Make sure the backend is running!')
    }
  }

  const handleStop = async () => {
    try {
      await axios.post(`${API_URL}/camera/stop`)
      setIsRunning(false)
      if (wsRef.current) {
        wsRef.current.close()
      }
    } catch (error) {
      console.error('Failed to stop camera:', error)
    }
  }

  const handleReset = async () => {
    try {
      const response = await axios.post(`${API_URL}/reset`)
      setStats(response.data.stats)
    } catch (error) {
      console.error('Failed to reset stats:', error)
    }
  }

  // Conditional rendering based on showStartup
  if (showStartup) {
    return <StartupPage onStart={handleStartApp} />
  }

  return (
    <div className="app">
      {/* HEADER */}
      <header className="header">
        <h1>AI PUSH-UP TRACKER</h1>
      </header>

      {/* MAIN CONTENT - Two Column Layout */}
      <div className="main-content">
        {/* LEFT COLUMN - Camera Feed */}
        <div className="left-column">
          <div className="camera-title">
            <h2>📹 LIVE FEED</h2>
          </div>
          <CameraFeed isRunning={isRunning} apiUrl={API_URL} />
        </div>

        {/* RIGHT COLUMN - Stats, Status & Controls */}
        <div className="right-column">
          {/* STATS GRID */}
          <div className="stats-grid">
            <StatCard
              title="FORM STATUS"
              value={stats.form_state.toUpperCase()}
              variant={stats.form_state.toLowerCase()}
            />
            <StatCard
              title="TOTAL REPS"
              value={stats.total_reps}
              variant="default"
            />
            <StatCard
              title="STAGE"
              value={stats.stage.toUpperCase()}
              variant="default"
            />
          </div>

          {/* CONTROLS */}
          <Controls
            isRunning={isRunning}
            onStart={handleStart}
            onStop={handleStop}
            onReset={handleReset}
            statusMessage={isRunning ? 'TRACKING ACTIVE' : 'READY TO START'}
            statusRunning={isRunning}
          />
        </div>
      </div>
    </div>
  )
}

export default App
