<script setup lang="ts">
import { computed, onMounted, ref } from 'vue'

interface Problem {
    slug: string
    number: number
    title: string
    difficulty: 'Easy' | 'Medium' | 'Hard'
    description: string
    patterns: string[]
    time_complexity: string
    space_complexity: string
    tests_passed: number
    total_tests: number
    solution_file: string
}

const problems = ref<Problem[]>([])
const loading = ref(true)
const error = ref('')
const selectedDifficulty = ref('All')

const filteredProblems = computed(() => {
  if (selectedDifficulty.value === 'All') {
    return problems.value
  }

  return problems.value.filter(
    (problem) => problem.difficulty === selectedDifficulty.value,
  )
})

onMounted(async () => {
  try {
    const response = await fetch(
      'http://127.0.0.1:8000/api/problems',
    )

    if (!response.ok) {
      throw new Error('Failed to load problems')
    }

    problems.value = await response.json()
  } catch (err) {
    error.value = 'Unable to load problems.'
  } finally {
    loading.value = false
  }
})
</script>

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
        <button
            class="filter"
            :class="{ active: selectedDifficulty === 'All' }"
            @click="selectedDifficulty = 'All'"
        >
        All
        </button>

        <button
            class="filter"
            :class="{ active: selectedDifficulty === 'Easy' }"
            @click="selectedDifficulty = 'Easy'"
        >
            Easy
        </button>

        <button
            class="filter"
            :class="{ active: selectedDifficulty === 'Medium' }"
            @click="selectedDifficulty = 'Medium'"
        >
            Medium
        </button>

        <button
            class="filter"
            :class="{ active: selectedDifficulty === 'Hard' }"
            @click="selectedDifficulty = 'Hard'"
        >
            Hard
        </button>
    </div>

    <div v-if="loading" class="loading">
      Loading problems...
    </div>

    <div v-else-if="error" class="error">
      {{ error }}
    </div>

    <div v-else class="problem-list">
      <RouterLink
        v-for="problem in filteredProblems"
        :key="problem.number"
        :to="`/problems/${problem.slug}`"
        class="problem-card"
      >
        <div class="problem-number">{{ problem.number }}</div>

        <div class="problem-content">
          <div class="problem-title-row">
            <h2>{{ problem.title }}</h2>
            <span :class="`difficulty ${problem.difficulty.toLowerCase()}`">
              {{ problem.difficulty }}
            </span>
          </div>

          <p>
            {{ problem.description }}
          </p>

          <div class="tags">
            <span v-for="pattern in problem.patterns" :key="pattern">
              {{ pattern }}
            </span>
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