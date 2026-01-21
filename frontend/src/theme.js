// Theme configuration for color scheme switching

export const themes = {
  colorful: {
    name: '🌈 COLORFUL',
    colors: {
      '--neo-yellow': '#FFE66D',
      '--neo-pink': '#FF6B9D',
      '--neo-cyan': '#00F5FF',
      '--neo-green': '#4ADE80',
      '--neo-red': '#FF5757',
      '--neo-purple': '#A78BFA',
      '--neo-orange': '#FB923C',
      '--neo-black': '#000000',
      '--neo-white': '#FFFFFF',
    },
    bodyBg: '#FFE66D',
    buttons: {
      start: '#4ADE80',
      stop: '#FF5757',
      reset: '#A78BFA',
      stopTextColor: '#000000',
    },
    statCards: {
      correct: '#4ADE80',
      wrong: '#FF5757',
      neutral: '#00F5FF',
      wrongTextColor: '#000000',
    },
    statusIndicator: {
      running: '#4ADE80',
      stopped: '#FF5757',
    },
    startupCards: {
      yellow: '#FFE66D',
      cyan: '#00F5FF',
      pink: '#FF6B9D',
      green: '#4ADE80',
      purple: '#A78BFA',
      orange: '#FB923C',
    },
  },
  blackwhite: {
    name: '⚪ B&W RETRO',
    colors: {
      '--neo-yellow': '#E8E8E8',
      '--neo-pink': '#B0B0B0',
      '--neo-cyan': '#D0D0D0',
      '--neo-green': '#C0C0C0',
      '--neo-red': '#707070',
      '--neo-purple': '#A0A0A0',
      '--neo-orange': '#909090',
      '--neo-black': '#000000',
      '--neo-white': '#FFFFFF',
    },
    bodyBg: '#E8E8E8',
    buttons: {
      start: '#FFFFFF',
      stop: '#505050',
      reset: '#B0B0B0',
      stopTextColor: '#FFFFFF',
    },
    statCards: {
      correct: '#FFFFFF',
      wrong: '#606060',
      neutral: '#D0D0D0',
      wrongTextColor: '#FFFFFF',
    },
    statusIndicator: {
      running: '#FFFFFF',
      stopped: '#404040',
    },
    startupCards: {
      yellow: '#F5F5F5',
      cyan: '#E0E0E0',
      pink: '#D5D5D5',
      green: '#EBEBEB',
      purple: '#C8C8C8',
      orange: '#DADADA',
    },
  },
  dark: {
    name: '🌙 DARK MODE',
    colors: {
      '--neo-yellow': '#2A2A2A',
      '--neo-pink': '#3A3A3A',
      '--neo-cyan': '#404040',
      '--neo-green': '#505050',
      '--neo-red': '#606060',
      '--neo-purple': '#4A4A4A',
      '--neo-orange': '#555555',
      '--neo-black': '#FFFFFF',
      '--neo-white': '#1A1A1A',
    },
    bodyBg: '#2A2A2A',
    buttons: {
      start: '#505050',
      stop: '#F0F0F0',
      reset: '#707070',
      stopTextColor: '#000000',
    },
    statCards: {
      correct: '#505050',
      wrong: '#F0F0F0',
      neutral: '#404040',
      wrongTextColor: '#000000',
    },
    statusIndicator: {
      running: '#EEEEEE',
      stopped: '#505050',
    },
    startupCards: {
      yellow: '#2A2A2A',
      cyan: '#353535',
      pink: '#303030',
      green: '#3A3A3A',
      purple: '#404040',
      orange: '#383838',
    },
  },
};

export const applyTheme = (themeName) => {
  const theme = themes[themeName];
  if (!theme) return;

  const root = document.documentElement;

  // Apply CSS variables
  Object.entries(theme.colors).forEach(([key, value]) => {
    root.style.setProperty(key, value);
  });

  // Apply body background
  document.body.style.backgroundColor = theme.bodyBg;

  // Store theme preference
  localStorage.setItem('colorScheme', themeName);
};

export const getCurrentTheme = () => {
  return localStorage.getItem('colorScheme') || 'blackwhite';
};
