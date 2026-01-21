function StatCard({ title, value, variant = 'default' }) {
  const getClassName = () => {
    const baseClass = 'stat-card'
    if (variant === 'correct' || variant === 'wrong' || variant === 'neutral') {
      return `${baseClass} ${variant}`
    }
    return baseClass
  }

  return (
    <div className={getClassName()}>
      <h2>{value}</h2>
      <p>{title}</p>
    </div>
  )
}

export default StatCard
