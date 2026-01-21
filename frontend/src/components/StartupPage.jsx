import { useState, useEffect } from 'react'
import './StartupPage.css'

function StartupPage({ onStart }) {
  const [understood, setUnderstood] = useState(false)
  const [colorScheme, setColorScheme] = useState('blackwhite') // default to current

  // Load saved color scheme from localStorage
  useEffect(() => {
    const saved = localStorage.getItem('colorScheme')
    if (saved) {
      setColorScheme(saved)
      applyColorScheme(saved)
    } else {
      applyColorScheme('blackwhite')
    }
  }, [])

  const applyColorScheme = (scheme) => {
    const root = document.documentElement
    
    // Set data attribute for theme-specific styles
    document.body.setAttribute('data-theme', scheme)
    
    if (scheme === 'colorful') {
      // Original colorful neobrutalism
      root.style.setProperty('--neo-yellow', '#FFE66D')
      root.style.setProperty('--neo-pink', '#FF6B9D')
      root.style.setProperty('--neo-cyan', '#00F5FF')
      root.style.setProperty('--neo-green', '#4ADE80')
      root.style.setProperty('--neo-red', '#FF5757')
      root.style.setProperty('--neo-purple', '#A78BFA')
      root.style.setProperty('--neo-orange', '#FB923C')
      root.style.setProperty('--neo-black', '#000000')
      root.style.setProperty('--neo-white', '#FFFFFF')
    } else if (scheme === 'blackwhite') {
      // Black & white retro
      root.style.setProperty('--neo-yellow', '#E8E8E8')
      root.style.setProperty('--neo-pink', '#B0B0B0')
      root.style.setProperty('--neo-cyan', '#D0D0D0')
      root.style.setProperty('--neo-green', '#C0C0C0')
      root.style.setProperty('--neo-red', '#707070')
      root.style.setProperty('--neo-purple', '#A0A0A0')
      root.style.setProperty('--neo-orange', '#909090')
      root.style.setProperty('--neo-black', '#000000')
      root.style.setProperty('--neo-white', '#FFFFFF')
    } else if (scheme === 'dark') {
      // Dark mode - Optimized with better contrast
      root.style.setProperty('--neo-yellow', '#1E1E1E')      // Very dark bg
      root.style.setProperty('--neo-pink', '#2D2D2D')        // Dark gray
      root.style.setProperty('--neo-cyan', '#3A3A3A')        // Medium-dark gray
      root.style.setProperty('--neo-green', '#4A4A4A')       // Medium gray
      root.style.setProperty('--neo-red', '#2A2A2A')         // Dark bg variant
      root.style.setProperty('--neo-purple', '#353535')      // Dark-medium gray
      root.style.setProperty('--neo-orange', '#404040')      // Medium-dark gray
      root.style.setProperty('--neo-black', '#FFFFFF')       // White borders/text
      root.style.setProperty('--neo-white', '#252525')       // Dark card background
    }
    
    // Update body background
    document.body.style.backgroundColor = scheme === 'dark' ? '#1E1E1E' : 
                                         scheme === 'colorful' ? '#FFE66D' : '#E8E8E8'
  }

  const handleColorSchemeChange = () => {
    const schemes = ['colorful', 'blackwhite', 'dark']
    const currentIndex = schemes.indexOf(colorScheme)
    const nextScheme = schemes[(currentIndex + 1) % schemes.length]
    
    setColorScheme(nextScheme)
    applyColorScheme(nextScheme)
    localStorage.setItem('colorScheme', nextScheme)
  }

  const getSchemeLabel = () => {
    switch(colorScheme) {
      case 'colorful': return '🌈 Neo'
      case 'blackwhite': return '⚪ B&W RETRO'
      case 'dark': return '🌙 DARK MODE'
      default: return 'THEME'
    }
  }

  const handleStartClick = () => {
    console.log('StartupPage: Let\'s Go button clicked, understood:', understood)
    if (understood && onStart) {
      console.log('StartupPage: Calling onStart function')
      onStart()
    } else {
      console.log('StartupPage: Button disabled or onStart not provided')
    }
  }

  return (
    <div className="startup-page">
      <div className="startup-container">
        {/* Header with Color Scheme Button */}
        <div className="startup-header">
          <div className="header-top">
            <h1>🎯 AI PUSH-UP TRACKER</h1>
            <button 
              className="color-scheme-btn"
              onClick={handleColorSchemeChange}
              title="Change color scheme"
            >
              {getSchemeLabel()}
            </button>
          </div>
          <p className="startup-subtitle">GET READY TO CRUSH IT!</p>
        </div>

        {/* Instructions Grid */}
        <div className="instructions-grid">
          {/* Instruction Card 1 */}
          <div className="instruction-card card-yellow">
            <div className="card-icon">💡</div>
            <h2>LIGHTING</h2>
            <p>Ensure you have <strong>mild, even lighting</strong> in your workout area. Avoid harsh shadows or backlighting.</p>
          </div>

          {/* Instruction Card 2 */}
          <div className="instruction-card card-cyan">
            <div className="card-icon">📹</div>
            <h2>CAMERA POSITION</h2>
            <p>Position yourself <strong>SIDEWAYS</strong> to the camera. Your full body should be visible from head to toe.</p>
          </div>

          {/* Instruction Card 3 */}
          <div className="instruction-card card-pink">
            <div className="card-icon">📏</div>
            <h2>DISTANCE</h2>
            <p>Stand <strong>6-8 feet away</strong> from the camera. Make sure there's enough space around you.</p>
          </div>

          {/* Instruction Card 4 */}
          <div className="instruction-card card-green">
            <div className="card-icon">👕</div>
            <h2>CLOTHING</h2>
            <p>Wear <strong>fitted clothing</strong> for better pose detection. Avoid loose or baggy clothes.</p>
          </div>

          {/* Instruction Card 5 */}
          <div className="instruction-card card-purple">
            <div className="card-icon">🎵</div>
            <h2>ENVIRONMENT</h2>
            <p>Choose a <strong>clear, uncluttered space</strong>. Remove obstacles that might interfere with tracking.</p>
          </div>

          {/* Instruction Card 6 */}
          <div className="instruction-card card-orange">
            <div className="card-icon">⚡</div>
            <h2>FORM FIRST</h2>
            <p><strong>Quality over quantity!</strong> Maintain proper form for accurate rep counting and feedback.</p>
          </div>
        </div>

        {/* Important Notes */}
        <div className="important-notes">
          <h3>⚠️ IMPORTANT NOTES</h3>
          <ul>
            <li>The AI tracks your body position in real-time</li>
            <li>Green indicates correct form, Red indicates incorrect form</li>
            <li>Your camera must remain stable during workout</li>
            <li>Allow camera permissions when prompted</li>
          </ul>
        </div>

        {/* Checkbox and Start Button */}
        <div className="startup-footer">
          <label className="checkbox-container">
            <input 
              type="checkbox" 
              checked={understood}
              onChange={(e) => setUnderstood(e.target.checked)}
            />
            <span className="checkbox-label">
              I understand the setup requirements and I'm ready to start
            </span>
          </label>

          <button 
            className={`start-button ${understood ? 'active' : 'disabled'}`}
            onClick={handleStartClick}
            disabled={!understood}
          >
            <span className="button-icon">🚀</span>
            LET'S GO!
          </button>
        </div>

        {/* Watermark Footer */}
        <div className="watermark-footer">
          <p>© 2025 AIPT by Exowdious</p>
        </div>
      </div>
    </div>
  )
}

export default StartupPage
