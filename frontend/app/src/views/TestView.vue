<template>
  <main class="container mx-auto my-12 px-4 text-high-contrast-text dark:text-d-high-contrast-text md:px-8 lg:px-16">
    <!-- Titre Principal de la Page -->
    <div class="mb-12 flex w-full items-center justify-center">
      <h1 class="border-b-2 border-accent-color pb-2 text-4xl font-extrabold text-high-contrast-text dark:border-d-accent-color dark:text-d-high-contrast-text">Try It Out</h1>
    </div>

    <!-- Description -->
    <section class="mb-12">
      <p class="text-lg text-low-contrast-text dark:text-d-low-contrast-text">
        Solve your quadratic or linear equations using Computorv1. Enter an equation below and click the "Solve" button to see the result.
      </p>
    </section>

    <!-- Input and Button -->
    <section class="mb-12 flex flex-col items-center gap-4">
      <input
        id="test-input"
        type="text"
        placeholder="Enter your equation (e.g., 2x^2 - 4x - 6)"
        class="w-full max-w-md rounded-lg border-2 border-ui-border bg-white px-4 py-2 text-lg text-high-contrast-text focus:outline-none focus:ring-2 focus:ring-accent-color dark:border-d-ui-border dark:bg-gray-800 dark:text-d-low-contrast-text dark:focus:ring-d-accent-color"
        :disabled="isLoading"
      />
      <button
        @click="makeRequests"
        class="hover:bg-accent-color-dark dark:hover:bg-d-accent-color-dark rounded-full bg-accent-color px-6 py-2 font-semibold text-white transition-colors dark:bg-d-accent-color"
        :disabled="isLoading"
      >
        Solve
      </button>
    </section>

    <!-- Loading Indicator -->
    <section v-if="isLoading" class="mb-12 flex justify-center">
      <div class="animate-spin">
        <SpinnerSvg custom="text-accent-color dark:text-d-accent-color size-16"/>
      </div>
    </section>

    <!-- Error Message -->
    <section v-if="error" class="mb-12">
      <div class="dark:border-d-red-500 dark:bg-d-red-50 dark:text-d-red-500 rounded-md border-l-4 border-red-500 bg-red-50 p-4 text-red-500 shadow-md dark:bg-gray-800">
        <h2 class="text-xl font-semibold">Error</h2>
        <p>{{ error }}</p>
      </div>
    </section>

    <!-- Display Results -->
    <section>
      <transition name="fade">
        <div v-if="result" key="result">
          <h2 class="mb-4 text-2xl font-semibold text-high-contrast-text dark:text-d-high-contrast-text">Results</h2>

          <!-- Degree 0 -->
          <div v-if="result.degree === 0" class="rounded-md border-l-4 border-accent-color bg-gray-50 p-4 shadow-md dark:border-d-accent-color dark:bg-gray-800">
            <p class="text-lg text-low-contrast-text dark:text-d-low-contrast-text">The equation has no solutions (constant equation).</p>
          </div>

          <!-- Degree 1 -->
          <div v-if="result.degree === 1" class="rounded-md border-l-4 border-accent-color bg-gray-50 p-4 shadow-md dark:border-d-accent-color dark:bg-gray-800">
            <p class="text-lg text-low-contrast-text dark:text-d-low-contrast-text">
              The equation has one solution: <span class="font-bold text-high-contrast-text dark:text-d-low-contrast-text">x = {{ result.x }}</span>
            </p>
          </div>

          <!-- Degree 2 with Δ -->
          <div v-if="result.degree === 2" class="rounded-md border-l-4 border-accent-color bg-gray-50 p-4 shadow-md dark:border-d-accent-color dark:bg-gray-800">
            <p class="text-lg text-low-contrast-text dark:text-d-low-contrast-text">
              The equation has {{ result.has_solution ? 'solutions' : 'no solutions' }}.
              <span v-if="result.delta !== undefined" class="font-bold text-high-contrast-text dark:text-d-low-contrast-text">Δ = {{ result.delta }}</span>
            </p>
            <div v-if="result.has_solution" class="mt-4">
              <p class="text-lg text-low-contrast-text dark:text-d-low-contrast-text">
                x<sub>1</sub> = {{ result.x1 }}<br />
                x<sub>2</sub> = {{ result.x2 }}
              </p>
            </div>
          </div>

          <!-- Degree > 2 -->
          <div v-if="result.degree > 2" class="rounded-md border-l-4 border-accent-color bg-gray-50 p-4 shadow-md dark:border-d-accent-color dark:bg-gray-800">
            <p class="text-lg text-low-contrast-text dark:text-d-low-contrast-text">
              The equation has a degree higher than 2 and cannot be solved by this tool.
            </p>
          </div>
        </div>
      </transition>
    </section>
  </main>
</template>

<script setup lang="ts">
import SpinnerSvg from '@/svg/SpinnerSvg.vue';
import { ref } from 'vue';

const result = ref<any>(null);
const isLoading = ref(false);
const error = ref<string | null>(null);

const makeRequests = async () => {
  isLoading.value = true;
  error.value = null; // Clear previous errors
  result.value = null;
  await new Promise((resolve) => setTimeout(resolve, 1000));
  const input = document.getElementById("test-input") as HTMLInputElement;
  const text = input?.value || '';
  const url = "http://127.0.0.1:4000/solve";

  try {
    const response = await fetch(url, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ content: text }),
    });

    if (!response.ok) {
      throw new Error('Network response was not ok');
    }

    const data = await response.json();
    result.value = data;
  } catch (e: any) {
    error.value = e.message || 'An unknown error occurred';
  } finally {
    isLoading.value = false;
  }
};
</script>

<style scoped>
/* Add some transition effects */
.fade-enter-active, .fade-leave-active {
  transition: opacity 0.5s;
}
.fade-enter, .fade-leave-to /* .fade-leave-active in <2.1.8 */ {
  opacity: 0;
}

/* Loading spinner styles */
.animate-spin {
  animation: spin 2s linear infinite;
}
@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}
</style>
