<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { useRoute } from 'vue-router'

interface Problem {
  number: number
  title: string
  difficulty: 'Easy' | 'Medium' | 'Hard'
  description: string
  approach: string
  patterns: string[]
  time_complexity: string
  space_complexity: string
  tests_passed: number
  total_tests: number
  solution: string
}

const route = useRoute()

const problem = ref<Problem | null>(null)
const loading = ref(true)
const error = ref('')

onMounted(async () => {
  try {
    const slug = route.params.slug

    const response = await fetch(
      `http://127.0.0.1:8000/api/problems/${slug}`,
    )

    if (!response.ok) {
      throw new Error('Problem not found')
    }

    problem.value = await response.json()
  } catch (err) {
    error.value = 'Unable to load problem.'
  } finally {
    loading.value = false
  }
})
</script>

<template>
  <section class="problem-detail">
    <RouterLink to="/problems" class="back-link">
      ← Back to Problems
    </RouterLink>

    <div v-if="loading" class="loading">
      Loading problem...
    </div>

    <div v-else-if="error" class="error">
      {{ error }}
    </div>

    <template v-else-if="problem">
      <div class="header">
        <div>
          <p class="eyebrow">ALGORITHM</p>

          <h1>{{ problem.title }}</h1>

          <div class="meta">
            <span class="difficulty">{{ problem.difficulty }}</span>

            <span
              v-for="pattern in problem.patterns"
              :key="pattern"
            >
              {{ pattern }}
            </span>
          </div>
        </div>

        <div class="status">
          ✓ Completed
        </div>
      </div>

      <div class="content-grid">
        <main>
          <section class="card">
            <h2>Problem</h2>

            <p>
              {{ problem.description }}
            </p>
          </section>

          <section class="card">
            <h2>Approach</h2>

            <p>
              {{ problem.approach }}
            </p>
          </section>

          <section class="card">
            <h2>Python Solution</h2>

            <pre><code>{{ problem.solution }}</code></pre>
          </section>
        </main>

        <aside>
          <section class="card">
            <h2>Complexity</h2>

            <div class="complexity">
              <div>
                <span>Time</span>
                <strong>{{ problem.time_complexity }}</strong>
              </div>

              <div>
                <span>Space</span>
                <strong>{{ problem.space_complexity }}</strong>
              </div>
            </div>
          </section>

          <section class="card">
            <h2>Tests</h2>

            <p class="test-result">
              ✓ {{ problem.tests_passed }} /
              {{ problem.total_tests }} tests passed
            </p>
          </section>

          <section class="card">
            <h2>My Notes</h2>

            <textarea
              placeholder="Write your notes about this algorithm..."
            ></textarea>
          </section>
        </aside>
      </div>
    </template>
  </section>
</template>

<style scoped>
.problem-detail {
  max-width: 1100px;
  margin: 0 auto;
}

.back-link {
  display: inline-block;
  margin-bottom: 30px;
  color: #94a3b8;
  text-decoration: none;
}

.back-link:hover {
  color: #38bdf8;
}

.eyebrow {
  margin: 0 0 8px;
  color: #38bdf8;
  font-size: 12px;
  font-weight: 700;
  letter-spacing: 1.5px;
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: flex-end;
  gap: 30px;
  margin-bottom: 35px;
}

h1 {
  margin: 0;
  font-size: 42px;
  color: #f8fafc;
}

.meta {
  display: flex;
  gap: 8px;
  margin-top: 15px;
}

.meta span {
  padding: 5px 10px;
  border-radius: 6px;
  background: #1e293b;
  color: #94a3b8;
  font-size: 12px;
}

.meta .difficulty {
  background: #052e16;
  color: #4ade80;
}

.status {
  color: #4ade80;
  font-size: 14px;
}

.content-grid {
  display: grid;
  grid-template-columns: 1fr 320px;
  gap: 20px;
}

.card {
  margin-bottom: 20px;
  padding: 24px;
  background: #111827;
  border: 1px solid #1e293b;
  border-radius: 12px;
}

.card h2 {
  margin: 0 0 15px;
  color: #f8fafc;
  font-size: 18px;
}

.card p {
  margin: 0;
  color: #94a3b8;
  line-height: 1.7;
}

pre {
  margin: 0;
  padding: 20px;
  overflow-x: auto;
  background: #0f172a;
  border-radius: 8px;
  border: 1px solid #1e293b;
}

code {
  color: #e2e8f0;
  font-family: "Cascadia Code", Consolas, monospace;
  font-size: 14px;
  line-height: 1.7;
}

.complexity {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.complexity div {
  display: flex;
  justify-content: space-between;
  color: #94a3b8;
}

.complexity strong {
  color: #38bdf8;
}

.test-result {
  color: #4ade80 !important;
}

textarea {
  width: 100%;
  min-height: 120px;
  padding: 12px;
  resize: vertical;
  box-sizing: border-box;
  border: 1px solid #334155;
  border-radius: 8px;
  background: #0f172a;
  color: #e2e8f0;
  font-family: inherit;
}

textarea:focus {
  outline: none;
  border-color: #38bdf8;
}

@media (max-width: 800px) {
  .header {
    align-items: flex-start;
    flex-direction: column;
  }

  .content-grid {
    grid-template-columns: 1fr;
  }
}
</style>