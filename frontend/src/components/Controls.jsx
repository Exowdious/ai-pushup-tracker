function Controls({ isRunning, onStart, onStop, onReset, statusMessage, statusRunning }) {
  return (
    <div className="controls">
      {/* STATUS BOX */}
      <div className="status-box-inline">
        <p>
          <span 
            className={`status-indicator ${statusRunning ? 'running' : 'stopped'}`}
          ></span>
          {statusMessage}
        </p>
      </div>

      <button
        className="btn btn-start"
        onClick={onStart}
        disabled={isRunning}
      >
        <span>🚀</span>
        START
      </button>

      <button
        className="btn btn-stop"
        onClick={onStop}
        disabled={!isRunning}
      >
        <span>⏸️</span>
        STOP
      </button>

      <button
        className="btn btn-reset"
        onClick={onReset}
      >
        <span>🔄</span>
        RESET
      </button>
    </div>
  )
}

export default Controls
