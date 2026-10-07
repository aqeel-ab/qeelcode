<template>
  <div class="app">
    <header class="navbar">
      <div class="logo">
        QeelCode
      </div>

      <nav>
        <RouterLink to="/">Dashboard</RouterLink>
        <RouterLink to="/problems">Problems</RouterLink>
        <RouterLink to="/patterns">Patterns</RouterLink>
        <RouterLink to="/notes">Notes</RouterLink>
        <RouterLink to="/progress">Progress</RouterLink>
      </nav>
    </header>

    <main>
      <RouterView />
    </main>
  </div>
</template>

<style scoped>
.app {
  min-height: 100vh;
  background: #0f172a;
  color: #e2e8f0;
}

.navbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 20px 40px;
  background: #09090b;
  border-bottom: 1px solid #1e293b;
}

.logo {
  font-size: 24px;
  font-weight: 700;
  color: #f8fafc;
}

nav {
  display: flex;
  gap: 28px;
}

nav a {
  color: #94a3b8;
  text-decoration: none;
  transition: color 0.2s ease;
}

nav a:hover,
nav a.router-link-active {
  color: #38bdf8;
}

main {
  min-height: calc(100vh - 73px);
  padding: 40px;
}
</style>