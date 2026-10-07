<script setup lang="ts">
import { ref } from 'vue'

const focusCompleted = ref(false)
const selectedActivity = ref<string | null>(null)

const activities = [
  {
    title: 'Two Sum',
    description: 'Completed problem',
  },
  {
    title: 'Sliding Window',
    description: 'Learned a new pattern',
  },
  {
    title: 'Binary Search',
    description: 'Added notes',
  },
]

function toggleFocus() {
  focusCompleted.value = !focusCompleted.value
}

function selectActivity(title: string) {
  selectedActivity.value =
    selectedActivity.value === title ? null : title
}
</script>

<template>
  <div class="dashboard">

    <!-- Hero -->
    <section class="hero">
      <div>
        <p class="eyebrow">YOUR ALGORITHM JOURNEY</p>

        <h1>Welcome back, Aimi.</h1>

        <p class="subtitle">
          Learn algorithms, understand patterns, and build your
          problem-solving skills.
        </p>
      </div>

      <div class="streak">
        <div class="streak-icon">🔥</div>

        <div>
          <span class="streak-number">7</span>
          <span class="streak-label">day streak</span>
        </div>
      </div>
    </section>

    <!-- Statistics -->
    <section class="stats">

      <div class="stat-card">
        <div class="stat-icon">✓</div>

        <div>
          <span class="stat-label">Problems Solved</span>
          <span class="stat-value">12</span>
        </div>

        <span class="stat-change">+3 this week</span>
      </div>

      <div class="stat-card">
        <div class="stat-icon">◇</div>

        <div>
          <span class="stat-label">Patterns Learned</span>
          <span class="stat-value">5</span>
        </div>

        <span class="stat-change">+2 this week</span>
      </div>

      <div class="stat-card">
        <div class="stat-icon">✎</div>

        <div>
          <span class="stat-label">Notes</span>
          <span class="stat-value">8</span>
        </div>

        <span class="stat-change">+1 this week</span>
      </div>

      <div class="stat-card">
        <div class="stat-icon">🔥</div>

        <div>
          <span class="stat-label">Current Streak</span>
          <span class="stat-value">7 days</span>
        </div>

        <span class="stat-change">Personal best</span>
      </div>

    </section>

    <!-- Main content -->
    <section class="content-grid">

      <!-- Today's Focus -->
      <div class="card focus-card">

        <div class="card-header">

          <div>
            <p class="eyebrow">CONTINUE LEARNING</p>
            <h2>Today's Focus</h2>
          </div>

          <span class="tag">Array</span>

        </div>

        <div class="focus-content">

          <div class="focus-number">
            01
          </div>

          <div>
            <h3>Two Pointer Pattern</h3>

            <p>
              Learn how two pointers can reduce the complexity
              of problems involving sorted arrays and sequences.
            </p>
          </div>

        </div>

        <!-- Progress -->
        <div class="progress-section">

          <div class="progress-info">
            <span>Learning progress</span>
            <span>{{ focusCompleted ? '100%' : '65%' }}</span>
          </div>

          <div class="progress-bar">
            <div
              class="progress-fill"
              :class="{ completed: focusCompleted }"
              :style="{ width: focusCompleted ? '100%' : '65%' }"
            ></div>
          </div>

        </div>

        <button
          class="primary-button"
          @click="toggleFocus"
        >
          {{ focusCompleted ? '✓ Completed' : 'Continue Learning →' }}
        </button>

      </div>

      <!-- Recent Activity -->
      <div class="card">

        <div class="card-header">

          <div>
            <p class="eyebrow">RECENT ACTIVITY</p>
            <h2>Your Progress</h2>
          </div>

          <span class="activity-count">
            {{ activities.length }}
          </span>

        </div>

        <div class="activity">

          <button
            v-for="activity in activities"
            :key="activity.title"
            class="activity-item"
            @click="selectActivity(activity.title)"
          >

            <span class="dot"></span>

            <div class="activity-content">
              <strong>{{ activity.title }}</strong>

              <p>{{ activity.description }}</p>

              <div
                v-if="selectedActivity === activity.title"
                class="activity-detail"
              >
                Opened from your recent learning activity.
              </div>
            </div>

            <span class="arrow">→</span>

          </button>

        </div>

      </div>

    </section>

    <!-- Learning Overview -->
    <section class="learning-section">

      <div class="section-heading">
        <div>
          <p class="eyebrow">YOUR LEARNING</p>
          <h2>Algorithm Progress</h2>
        </div>

        <span class="overall-progress">32%</span>
      </div>

      <div class="learning-grid">

        <div class="learning-item">
          <div class="learning-header">
            <span>Arrays</span>
            <span>70%</span>
          </div>

          <div class="progress-bar">
            <div
              class="progress-fill"
              style="width: 70%"
            ></div>
          </div>
        </div>

        <div class="learning-item">
          <div class="learning-header">
            <span>Searching</span>
            <span>45%</span>
          </div>

          <div class="progress-bar">
            <div
              class="progress-fill"
              style="width: 45%"
            ></div>
          </div>
        </div>

        <div class="learning-item">
          <div class="learning-header">
            <span>Sorting</span>
            <span>30%</span>
          </div>

          <div class="progress-bar">
            <div
              class="progress-fill"
              style="width: 30%"
            ></div>
          </div>
        </div>

        <div class="learning-item">
          <div class="learning-header">
            <span>Graphs</span>
            <span>15%</span>
          </div>

          <div class="progress-bar">
            <div
              class="progress-fill"
              style="width: 15%"
            ></div>
          </div>
        </div>

      </div>

    </section>

    <!-- Quick Actions -->
    <section class="quick-actions">

      <p class="eyebrow">QUICK ACTIONS</p>

      <div class="action-grid">

        <button class="action-card">
          <span class="action-icon">+</span>
          <div>
            <strong>Add Problem</strong>
            <small>Save a new algorithm problem</small>
          </div>
        </button>

        <button class="action-card">
          <span class="action-icon">✎</span>
          <div>
            <strong>Write a Note</strong>
            <small>Record something you learned</small>
          </div>
        </button>

        <button class="action-card">
          <span class="action-icon">◇</span>
          <div>
            <strong>Explore Patterns</strong>
            <small>Review algorithm patterns</small>
          </div>
        </button>

      </div>

    </section>

  </div>
</template>

<style scoped>
.dashboard {
  max-width: 1200px;
  margin: 0 auto;
}

/* Hero */

.hero {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 40px;
}

.eyebrow {
  margin: 0 0 10px;
  color: #38bdf8;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 1.5px;
}

h1 {
  margin: 0;
  color: #f8fafc;
  font-size: 40px;
}

.subtitle {
  margin-top: 12px;
  color: #94a3b8;
  font-size: 16px;
}

/* Streak */

.streak {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 16px 22px;
  background: #111113;
  border: 1px solid #27272a;
  border-radius: 14px;
  transition: 0.25s ease;
}

.streak:hover {
  border-color: #334155;
  transform: translateY(-2px);
}

.streak-icon {
  font-size: 24px;
}

.streak-number {
  display: block;
  color: #38bdf8;
  font-size: 25px;
  font-weight: 700;
}

.streak-label {
  color: #64748b;
  font-size: 12px;
}

/* Statistics */

.stats {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 16px;
  margin-bottom: 24px;
}

.stat-card {
  position: relative;
  display: flex;
  align-items: center;
  gap: 14px;
  padding: 20px;
  background: #111113;
  border: 1px solid #27272a;
  border-radius: 12px;
  transition: all 0.25s ease;
}

.stat-card:hover {
  border-color: #334155;
  transform: translateY(-3px);
  background: #131d2e;
}

.stat-icon {
  display: grid;
  place-items: center;
  width: 38px;
  height: 38px;
  border-radius: 9px;
  background: #0c4a6e;
  color: #7dd3fc;
  font-size: 17px;
}

.stat-label {
  display: block;
  color: #94a3b8;
  font-size: 12px;
}

.stat-value {
  display: block;
  margin-top: 4px;
  color: #f8fafc;
  font-size: 21px;
  font-weight: 700;
}

.stat-change {
  position: absolute;
  right: 14px;
  bottom: 12px;
  color: #38bdf8;
  font-size: 9px;
}

/* Cards */

.content-grid {
  display: grid;
  grid-template-columns: 1.4fr 1fr;
  gap: 20px;
}

.card {
  padding: 26px;
  background: #111113;
  border: 1px solid #27272a;
  border-radius: 14px;
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
}

.card h2 {
  margin: 0;
  color: #f8fafc;
  font-size: 19px;
}

.card h3 {
  margin: 0;
  color: #f8fafc;
  font-size: 23px;
}

.tag {
  padding: 5px 10px;
  border-radius: 6px;
  background: #0c4a6e;
  color: #7dd3fc;
  font-size: 11px;
}

/* Focus */

.focus-content {
  display: flex;
  gap: 18px;
  align-items: flex-start;
  margin-top: 30px;
}

.focus-number {
  color: #334155;
  font-size: 34px;
  font-weight: 700;
}

.focus-content p {
  margin-top: 8px;
  color: #94a3b8;
  line-height: 1.6;
}

.progress-section {
  margin-top: 25px;
}

.progress-info {
  display: flex;
  justify-content: space-between;
  margin-bottom: 8px;
  color: #64748b;
  font-size: 12px;
}

.progress-bar {
  width: 100%;
  height: 6px;
  overflow: hidden;
  border-radius: 20px;
  background: #27272a;
}

.progress-fill {
  height: 100%;
  border-radius: 20px;
  background: #38bdf8;
  transition: width 0.4s ease;
}

.progress-fill.completed {
  background: #22c55e;
}

.primary-button {
  margin-top: 22px;
  padding: 10px 17px;
  border: none;
  border-radius: 7px;
  background: #38bdf8;
  color: #082f49;
  font-weight: 700;
  cursor: pointer;
  transition: 0.2s ease;
}

.primary-button:hover {
  background: #7dd3fc;
  transform: translateY(-1px);
}

/* Activity */

.activity {
  margin-top: 20px;
}

.activity-item {
  display: flex;
  align-items: flex-start;
  gap: 12px;
  width: 100%;
  padding: 14px 0;
  border: none;
  border-bottom: 1px solid #27272a;
  background: transparent;
  color: inherit;
  text-align: left;
  cursor: pointer;
}

.activity-item:hover strong {
  color: #38bdf8;
}

.activity-content {
  flex: 1;
}

.activity-item strong {
  color: #e2e8f0;
  transition: color 0.2s ease;
}

.activity-item p {
  margin: 4px 0 0;
  color: #64748b;
  font-size: 12px;
}

.activity-detail {
  margin-top: 8px;
  color: #64748b;
  font-size: 11px;
}

.dot {
  width: 7px;
  height: 7px;
  margin-top: 6px;
  border-radius: 50%;
  background: #38bdf8;
}

.arrow {
  color: #475569;
  transition: 0.2s ease;
}

.activity-item:hover .arrow {
  color: #38bdf8;
  transform: translateX(3px);
}

.activity-count {
  padding: 4px 8px;
  border-radius: 6px;
  background: #27272a;
  color: #94a3b8;
  font-size: 11px;
}

/* Learning */

.learning-section {
  margin-top: 24px;
  padding: 26px;
  background: #111113;
  border: 1px solid #27272a;
  border-radius: 14px;
}

.section-heading {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 25px;
}

.section-heading h2 {
  margin: 0;
  color: #f8fafc;
  font-size: 19px;
}

.overall-progress {
  color: #38bdf8;
  font-size: 24px;
  font-weight: 700;
}

.learning-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 22px 35px;
}

.learning-header {
  display: flex;
  justify-content: space-between;
  margin-bottom: 8px;
  color: #94a3b8;
  font-size: 12px;
}

/* Quick actions */

.quick-actions {
  margin-top: 30px;
  margin-bottom: 30px;
}

.action-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 14px;
}

.action-card {
  display: flex;
  align-items: center;
  gap: 14px;
  padding: 17px;
  border: 1px solid #27272a;
  border-radius: 12px;
  background: #111113;
  color: #e2e8f0;
  text-align: left;
  cursor: pointer;
  transition: all 0.25s ease;
}

.action-card:hover {
  border-color: #38bdf8;
  background: #131d2e;
  transform: translateY(-2px);
}

.action-icon {
  display: grid;
  place-items: center;
  width: 35px;
  height: 35px;
  border-radius: 8px;
  background: #27272a;
  color: #38bdf8;
  font-size: 18px;
}

.action-card strong {
  display: block;
  font-size: 13px;
}

.action-card small {
  display: block;
  margin-top: 4px;
  color: #64748b;
  font-size: 10px;
}

/* Responsive */

@media (max-width: 900px) {
  .stats {
    grid-template-columns: repeat(2, 1fr);
  }

  .content-grid {
    grid-template-columns: 1fr;
  }

  .action-grid {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 600px) {
  .hero {
    flex-direction: column;
    align-items: flex-start;
  }

  .stats {
    grid-template-columns: 1fr;
  }

  .learning-grid {
    grid-template-columns: 1fr;
  }

  h1 {
    font-size: 32px;
  }
}
</style>