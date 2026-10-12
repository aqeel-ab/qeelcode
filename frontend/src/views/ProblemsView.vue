<template>
  <section class="problems-page">
    <div class="page-header">
      <div>
        <p class="eyebrow">ALGORITHM LIBRARY</p>
        <h1>Problems</h1>
        <p class="subtitle">
          Explore algorithms, understand the patterns, and review your solutions.
        </p>
      </div>

      <div class="progress-summary">
        <span>2 / 10 completed</span>
        <div class="progress-bar">
          <div class="progress-fill"></div>
        </div>
      </div>
    </div>

    <div class="filters">
      <button class="filter active">All</button>
      <button class="filter">Easy</button>
      <button class="filter">Medium</button>
      <button class="filter">Hard</button>
    </div>

    <div class="problem-list">
      <RouterLink to="/problems/two-sum" class="problem-card">
        <div class="problem-number">01</div>

        <div class="problem-content">
          <div class="problem-title-row">
            <h2>Two Sum</h2>
            <span class="difficulty easy">Easy</span>
          </div>

          <p>
            Find two numbers in an array that add up to a given target.
          </p>

          <div class="tags">
            <span>Array</span>
            <span>Hash Map</span>
          </div>
        </div>

        <div class="problem-status">
          <span class="completed">✓ Completed</span>
        </div>
      </RouterLink>

      <RouterLink to="/problems/add-two-numbers" class="problem-card">
        <div class="problem-number">02</div>

        <div class="problem-content">
          <div class="problem-title-row">
            <h2>Add Two Numbers</h2>
            <span class="difficulty medium">Medium</span>
          </div>

          <p>
            Add two numbers represented by linked lists and return the result.
          </p>

          <div class="tags">
            <span>Linked List</span>
            <span>Math</span>
          </div>
        </div>

        <div class="problem-status">
          <span class="completed">✓ Completed</span>
        </div>
      </RouterLink>
    </div>
  </section>
</template>

<style scoped>
.problems-page {
  max-width: 1100px;
  margin: 0 auto;
}

.page-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-end;
  gap: 40px;
  margin-bottom: 40px;
}

.eyebrow {
  margin: 0 0 8px;
  font-size: 12px;
  font-weight: 700;
  letter-spacing: 1.5px;
  color: #38bdf8;
}

h1 {
  margin: 0;
  font-size: 42px;
  color: #f8fafc;
}

.subtitle {
  margin: 12px 0 0;
  color: #94a3b8;
  font-size: 16px;
}

.progress-summary {
  min-width: 180px;
  color: #94a3b8;
  font-size: 14px;
}

.progress-bar {
  height: 6px;
  margin-top: 10px;
  background: #1e293b;
  border-radius: 999px;
  overflow: hidden;
}

.progress-fill {
  width: 20%;
  height: 100%;
  background: #38bdf8;
}

.filters {
  display: flex;
  gap: 10px;
  margin-bottom: 24px;
}

.filter {
  padding: 8px 18px;
  border: 1px solid #334155;
  border-radius: 8px;
  background: #111827;
  color: #94a3b8;
  cursor: pointer;
}

.filter:hover,
.filter.active {
  border-color: #38bdf8;
  color: #38bdf8;
}

.problem-list {
  display: flex;
  flex-direction: column;
  gap: 14px;
}

.problem-card {
  display: grid;
  grid-template-columns: 60px 1fr auto;
  gap: 20px;
  align-items: center;
  padding: 24px;
  background: #111827;
  border: 1px solid #1e293b;
  border-radius: 12px;
  text-decoration: none;
  color: inherit;
  transition:
    transform 0.2s ease,
    border-color 0.2s ease;
}

.problem-card:hover {
  transform: translateY(-2px);
  border-color: #334155;
}

.problem-number {
  color: #64748b;
  font-size: 14px;
  font-weight: 700;
}

.problem-title-row {
  display: flex;
  align-items: center;
  gap: 12px;
}

h2 {
  margin: 0;
  font-size: 18px;
  color: #f8fafc;
}

.problem-content p {
  margin: 8px 0 12px;
  color: #94a3b8;
  font-size: 14px;
}

.difficulty,
.tags span {
  display: inline-block;
  padding: 4px 9px;
  border-radius: 6px;
  font-size: 12px;
}

.easy {
  background: #052e16;
  color: #4ade80;
}

.medium {
  background: #451a03;
  color: #fbbf24;
}

.tags {
  display: flex;
  gap: 8px;
}

.tags span {
  background: #1e293b;
  color: #94a3b8;
}

.problem-status {
  white-space: nowrap;
}

.completed {
  color: #4ade80;
  font-size: 13px;
}

@media (max-width: 700px) {
  .page-header {
    flex-direction: column;
    align-items: flex-start;
  }

  .problem-card {
    grid-template-columns: 1fr;
  }

  .problem-number {
    display: none;
  }
}
</style>