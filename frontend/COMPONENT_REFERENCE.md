# React Component Props Types Reference

## StatCard Component
```jsx
<StatCard 
  title="FORM STATUS"           // string (uppercase recommended)
  value={stats.form_state}      // string | number
  variant="correct"             // 'default' | 'correct' | 'wrong' | 'neutral'
/>
```

### Variants:
- `correct` - Green background (good form)
- `wrong` - Red background (bad form)
- `neutral` - Cyan background (neutral)
- `default` - White background

## CameraFeed Component
```jsx
<CameraFeed 
  isRunning={true}              // boolean
  apiUrl="http://localhost:8000" // string
/>
```

## Controls Component
```jsx
<Controls 
  isRunning={false}             // boolean
  onStart={handleStart}         // function
  onStop={handleStop}           // function
  onReset={handleReset}         // function
/>
```

# CSS Custom Properties (Neobrutalism Theme)

```css
--neo-black: #000000;   /* Borders & text */
--neo-white: #FFFFFF;   /* Card backgrounds */
--neo-yellow: #FFE66D;  /* Page background */
--neo-pink: #FF6B9D;    /* Accent color */
--neo-cyan: #00F5FF;    /* Buttons */
--neo-green: #4ADE80;   /* Correct form */
--neo-red: #FF5757;     /* Wrong form */
--neo-purple: #A78BFA;  /* Reset button */
--neo-orange: #FB923C;  /* Future use */
```

# API Response Formats

## GET /stats
```json
{
  "total_reps": 0,
  "form_state": "Neutral",
  "stage": "Up"
}
```

## POST /camera/start
```json
{
  "status": "started",
  "message": "Camera started successfully"
}
```

## WebSocket /ws/stats
Sends JSON every 100ms:
```json
{
  "total_reps": 5,
  "form_state": "Correct",
  "stage": "Down"
}
```
