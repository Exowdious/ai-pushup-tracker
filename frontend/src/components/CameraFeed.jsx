function CameraFeed({ isRunning, apiUrl }) {
  return (
    <div className="camera-container">
      <div className="camera-header">
        <span>📹</span>
        <h3>LIVE FEED</h3>
      </div>
      
      {isRunning ? (
        <img
          src={`${apiUrl}/video_feed`}
          alt="Camera Feed"
          className="camera-feed"
        />
      ) : (
        <div className="camera-placeholder">
          📷 PRESS START TO BEGIN
        </div>
      )}
    </div>
  )
}

export default CameraFeed
