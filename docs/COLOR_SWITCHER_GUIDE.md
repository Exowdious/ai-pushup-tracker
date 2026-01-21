# Color Scheme Switcher - User Guide

## 🎨 Three Themes Available

Your AI Push-Up Tracker now supports three distinct color schemes:

### 1. 🌈 COLORFUL (Original)
- **Vibrant neobrutalism** with bold, saturated colors
- Yellow background (#FFE66D)
- Bright green, pink, cyan, purple accents
- High energy, modern aesthetic
- Perfect for: Energetic workouts, motivation

### 2. ⚪ B&W RETRO (Current Default)
- **Monochrome elegance** with grayscale palette
- Light gray background (#E8E8E8)
- Black and white with subtle gray variations
- Classic, timeless design
- Perfect for: Minimalists, distraction-free training

### 3. 🌙 DARK MODE
- **Night-friendly** dark theme
- Dark gray background (#2A2A2A)
- White text on dark backgrounds
- Reduced eye strain in low light
- Perfect for: Evening workouts, dark environments

## 🔄 How to Switch Themes

### On Startup Page:
1. Look for the color scheme button in the top-right corner
2. Shows current theme: `🌈 COLORFUL`, `⚪ B&W RETRO`, or `🌙 DARK MODE`
3. Click to cycle through themes
4. Changes apply instantly across the entire app

### On Main Tracker:
- Theme indicator (emoji) appears next to the header title
- Preference is saved automatically
- Persists across browser sessions

## 🎯 Theme Details

### Button Colors:
| Element | Colorful | B&W Retro | Dark Mode |
|---------|----------|-----------|-----------|
| **Start** | Green | White | Medium Gray |
| **Stop** | Red | Dark Gray | Light Gray |
| **Reset** | Purple | Medium Gray | Gray |

### Stat Cards (Form Status):
| State | Colorful | B&W Retro | Dark Mode |
|-------|----------|-----------|-----------|
| **Correct** | Green | White | Medium Gray |
| **Wrong** | Red | Dark Gray | Light Gray |
| **Neutral** | Cyan | Light Gray | Dark Gray |

### Status Indicators:
- **Running**: Green / White / Light Gray
- **Stopped**: Red / Dark Gray / Medium Gray

## 💾 Automatic Saving

Your theme preference is automatically saved to browser localStorage:
- No need to log in
- Persists between visits
- Works across different tabs
- Clears only if you clear browser data

## 🔧 Technical Details

**Implementation:**
- Uses CSS custom properties (variables)
- Dynamic theme switching via JavaScript
- No page reload required
- Fully responsive across all screen sizes

**Files Modified:**
- `frontend/src/components/StartupPage.jsx` - Theme switcher logic
- `frontend/src/components/StartupPage.css` - Color scheme button styles
- `frontend/src/App.jsx` - Theme indicator
- `frontend/src/App.css` - Theme indicator styles
- `frontend/src/theme.js` - Theme configuration (optional reference)

## 📱 Mobile Responsive

- Color scheme button adapts to mobile screens
- Full-width on small devices
- Easy to tap with touch
- All themes optimized for mobile viewing

## 🎨 Customization

Want to create your own theme? Edit the `applyColorScheme` function in:
```javascript
frontend/src/components/StartupPage.jsx
```

Add a new case with your custom color values!

## 🐛 Troubleshooting

**Theme not saving?**
- Check browser localStorage is enabled
- Try clearing browser cache
- Refresh the page

**Colors look wrong?**
- Hard refresh: Cmd+Shift+R (Mac) or Ctrl+Shift+R (Windows)
- Check browser console for errors
- Ensure CSS files are loading

**Button not visible?**
- Check screen size (may be repositioned on mobile)
- Scroll to top of startup page
- Try zooming out

## 🎉 Enjoy Your Personalized Experience!

Choose the theme that motivates you best and crush those push-ups! 💪
