# Color Scheme Switch Guide

## Current Theme: Retro Black & White

Your app now uses a monochrome retro color scheme with black, white, and various shades of gray.

### Color Mapping:
- **Background**: Light gray (#E8E8E8) instead of yellow
- **Buttons**: 
  - Start: White (#FFFFFF)
  - Stop: Dark gray (#505050) with white text
  - Reset: Medium gray (#B0B0B0)
- **Stat Cards**:
  - Correct: White (#FFFFFF)
  - Wrong: Dark gray (#606060) with white text
  - Neutral: Light gray (#D0D0D0)
- **Startup Cards**: Various gray shades (#F5F5F5 to #C8C8C8)

## How to Revert to Colorful Theme

If you don't like the black & white scheme, here's how to restore the original colors:

### Option 1: Quick Revert (Recommended)
Run these commands in terminal:

```bash
cd /Users/exowdious/Documents/ai-pushup-tracker/frontend/src

# Restore App.css colors
sed -i.bak 's/--neo-yellow: #E8E8E8/--neo-yellow: #FFE66D/' App.css
sed -i.bak 's/--neo-pink: #B0B0B0/--neo-pink: #FF6B9D/' App.css
sed -i.bak 's/--neo-cyan: #D0D0D0/--neo-cyan: #00F5FF/' App.css
sed -i.bak 's/--neo-green: #C0C0C0/--neo-green: #4ADE80/' App.css
sed -i.bak 's/--neo-red: #707070/--neo-red: #FF5757/' App.css
sed -i.bak 's/--neo-purple: #A0A0A0/--neo-purple: #A78BFA/' App.css
sed -i.bak 's/--neo-orange: #909090/--neo-orange: #FB923C/' App.css
```

### Option 2: Manual Revert
Open these files and replace the grayscale values with original colors:

**`frontend/src/App.css` - Line 10-17:**
```css
--neo-yellow: #FFE66D;   /* was #E8E8E8 */
--neo-pink: #FF6B9D;     /* was #B0B0B0 */
--neo-cyan: #00F5FF;     /* was #D0D0D0 */
--neo-green: #4ADE80;    /* was #C0C0C0 */
--neo-red: #FF5757;      /* was #707070 */
--neo-purple: #A78BFA;   /* was #A0A0A0 */
--neo-orange: #FB923C;   /* was #909090 */
```

**`frontend/src/App.css` - Buttons (around line 356-363):**
```css
.btn-start {
  background-color: var(--neo-green);
}

.btn-stop {
  background-color: var(--neo-red);
  /* Remove: color: var(--neo-white); */
}

.btn-reset {
  background-color: var(--neo-purple);
}
```

**`frontend/src/App.css` - Stat Cards (around line 217-226):**
```css
.stat-card.correct {
  background-color: var(--neo-green);
}

.stat-card.wrong {
  background-color: var(--neo-red);
  /* Remove: color: var(--neo-white); */
}

.stat-card.neutral {
  background-color: var(--neo-cyan);
}
```

**`frontend/src/App.css` - Status Indicators (around line 388-394):**
```css
.status-indicator.running {
  background-color: var(--neo-green);
}

.status-indicator.stopped {
  background-color: var(--neo-red);
}
```

**`frontend/src/components/StartupPage.css` - Cards (around line 94-113):**
```css
.card-yellow {
  background-color: #FFE66D;
}

.card-cyan {
  background-color: #00F5FF;
}

.card-pink {
  background-color: #FF6B9D;
}

.card-green {
  background-color: #4ADE80;
}

.card-purple {
  background-color: #A78BFA;
}

.card-orange {
  background-color: #FB923C;
}
```

**`frontend/src/components/StartupPage.css` - Start Button (around line 247):**
```css
.start-button {
  background-color: var(--neo-green);
  /* Remove the hover background change and disabled dark gray */
}
```

### Option 3: Use Backup Files
Backup files with original colors are saved at:
- `frontend/src/App.css.colorful.backup`
- `frontend/src/components/StartupPage.css.colorful.backup`

You can reference these files to copy the original color values.

## Testing the Changes
After reverting, refresh your browser (Cmd+R or Ctrl+R) to see the colorful theme again.

## Notes
- The black & white theme maintains the same neobrutalism design style
- Only colors changed - layout, shadows, and borders remain the same
- All functionality works identically in both themes
