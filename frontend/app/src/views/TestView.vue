<template>
  <main class="container mx-auto my-12 px-4 text-high-contrast-text dark:text-d-high-contrast-text md:px-8 lg:px-16">
    <!-- Titre Principal de la Page -->
    <div class="mb-12 flex w-full items-center justify-center">
      <h1
        class="border-b-2 border-accent-color pb-2 text-4xl font-extrabold text-high-contrast-text dark:border-d-accent-color dark:text-d-high-contrast-text">
        Try It Out</h1>
    </div>

    <!-- Description -->
    <section class="mb-12">
      <p class="text-lg text-low-contrast-text dark:text-d-low-contrast-text">
        Solve your quadratic or linear equations using Computorv1. Enter an equation below and click the "Solve" button
        to see the result.
      </p>
    </section>

    <!-- Input and Button -->
    <section class="mb-12 flex flex-col items-center gap-4">
      <input id="test-input" type="text" placeholder="Enter your equation (e.g., 2x^2 - 4x - 6)"
        class="w-full max-w-md rounded-lg border-2 border-ui-border bg-white px-4 py-2 text-lg text-high-contrast-text focus:outline-none focus:ring-2 focus:ring-accent-color dark:border-d-ui-border dark:bg-gray-800 dark:text-d-low-contrast-text dark:focus:ring-d-accent-color"
        :disabled="isLoading" />
      <button @click="makeRequests"
        class="hover:bg-accent-color-dark dark:hover:bg-d-accent-color-dark rounded-full bg-accent-color px-6 py-2 font-semibold text-white transition-colors dark:bg-d-accent-color"
        :disabled="isLoading">
        Solve
      </button>
    </section>

    <!-- Loading Indicator -->
    <section v-if="isLoading" class="mb-12 flex justify-center">
      <div class="animate-spin">
        <SpinnerSvg custom="text-accent-color dark:text-d-accent-color size-16" />
      </div>
    </section>

    <!-- Error Message -->
    <section v-if="error" class="mb-12">
      <div
        class="dark:border-d-red-500 dark:bg-d-red-50 dark:text-d-red-500 rounded-md border-l-4 border-red-500 bg-red-50 p-4 text-red-500 shadow-md dark:bg-gray-800">
        <h2 class="text-xl font-semibold">Error</h2>
        <p>{{ error }}</p>
      </div>
    </section>

    <!-- Display Results -->
    <section>
      <transition name="fade">
        <div v-if="result" key="result" class="flex flex-col gap-8">
          <div>
            <h2 class="mb-2 text-2xl font-semibold text-high-contrast-text dark:text-d-high-contrast-text">Informations
            </h2>
            <div
              class="rounded-md border-l-4 border-accent-color bg-gray-50 p-4 shadow-md dark:border-d-accent-color dark:bg-gray-800">
              <p class="text-lg text-low-contrast-text dark:text-d-low-contrast-text">Reduced form: <span
                  class="font-bold text-high-contrast-text dark:text-d-low-contrast-text">{{ result.equation }}</span>
              </p>
              <p class="text-lg text-low-contrast-text dark:text-d-low-contrast-text">Polynomial degree: <span
                  class="font-bold text-high-contrast-text dark:text-d-low-contrast-text">{{ result.degree }}</span></p>
              <p v-if="result.degree == 2" class="text-lg text-low-contrast-text dark:text-d-low-contrast-text">Δ = {{ result.b }}<sup>2</sup> - 4 * {{ result.a }} * {{ result.c }} = <span class="font-bold text-high-contrast-text dark:text-d-low-contrast-text">{{ result.delta }}</span></p>
            </div>
          </div>
          <div>
            <h2 class="mb-2 text-2xl font-semibold text-high-contrast-text dark:text-d-high-contrast-text">Results</h2>

            <!-- Degree 0 -->
            <div v-if="result.degree === 0"
              class="rounded-md border-l-4 border-accent-color bg-gray-50 p-4 shadow-md dark:border-d-accent-color dark:bg-gray-800">

              <p v-if="result.has_solution" class="text-lg text-low-contrast-text dark:text-d-low-contrast-text">All
                values of <span class="font-bold text-high-contrast-text dark:text-d-low-contrast-text">x</span> are
                solutions.</p>
              <p v-else class="text-lg text-low-contrast-text dark:text-d-low-contrast-text">The equation has no
                solutions.</p>
            </div>

            <!-- Degree 1 -->
            <div v-if="result.degree === 1"
              class="rounded-md border-l-4 border-accent-color bg-gray-50 p-4 shadow-md dark:border-d-accent-color dark:bg-gray-800">
              <div v-if="result.has_solution" class="text-lg text-low-contrast-text dark:text-d-low-contrast-text">
                The equation has one solution:
                <div v-if="result.irreducible" class="flex flex-row items-center gap-1">
                  <p>x = <span class="font-bold">-</span></p>
                      <div class="flex flex-col items-center justify-center font-bold">
                        <p class=" translate-y-[2px]">{{ result.b }}</p>
                        <div class=" h-[2px] w-full translate-y-[2px] bg-low-contrast-text dark:bg-d-low-contrast-text"></div>
                        <p class=" translate-y-[2px]">{{result.a }}</p>
                      </div>
                      <div >

                      </div>
                </div>
                <div v-else>
                  <p>x = <span class="font-bold">{{ result.x }}</span></p>
                </div>


              </div>
              <p v-else class="text-lg text-low-contrast-text dark:text-d-low-contrast-text">The equation has no
                solutions.</p>
            </div>

            <!-- Degree 2 with Δ -->
            <div v-if="result.degree === 2"
              class="rounded-md border-l-4 border-accent-color bg-gray-50 p-4 shadow-md dark:border-d-accent-color dark:bg-gray-800">
              <div v-if="result.has_solution && result.delta >= 0" class="text-lg text-low-contrast-text dark:text-d-low-contrast-text">
                <p v-if="result.delta == 0">The equation has one solution. <span class="font-bold text-high-contrast-text dark:text-d-low-contrast-text">Δ = 0</span></p>
                <p v-else>The equation has two solutions. <span class="font-bold text-high-contrast-text dark:text-d-low-contrast-text">Δ > 0</span></p>
              </div>
              <div v-else class="text-lg text-low-contrast-text dark:text-d-low-contrast-text">
                <!--eslint-disable-next-line vue/no-parsing-error-->
                <p>The equation has no solutions. <span class="font-bold text-high-contrast-text dark:text-d-low-contrast-text">Δ < 0</span></p>
              </div>
              <div v-if="result.has_solution && result.delta >= 0" class="mt-4">
                <div v-if="result.delta > 0">

                  <div class="text-lg text-low-contrast-text dark:text-d-low-contrast-text">

                    <div class="flex flex-row items-center gap-1">
                      <p>x<sub>1</sub> = </p>
                      <div v-if="result.irreducible_x1" class="flex flex-col items-center justify-center font-bold">
                        <p class=" translate-y-[2px]"><span v-if="result.b > 0" >-</span> {{ result.b > 0 ? result.b : Math.abs(result.b) }} - √{{ result.delta }}</p>
                        <div class=" h-[2px] w-full translate-y-[2px] bg-low-contrast-text dark:bg-d-low-contrast-text"></div>
                        <p class=" translate-y-[2px]">{{ 2 * result.a }}</p>
                      </div>
                      <div v-else>
                        <span class="font-bold">{{ result.x1 }}</span>
                      </div>
                    </div>

                    <div class="flex flex-row items-center gap-1">
                      <p>x<sub>1</sub> = </p>
                      <div v-if="result.irreducible_x2" class="flex flex-col items-center justify-center font-bold">
                        <p class=" translate-y-[2px]"><span v-if="result.b > 0" >-</span> {{ result.b > 0 ? result.b : Math.abs(result.b) }} + √{{ result.delta }}</p>
                        <div class=" h-[2px] w-full translate-y-[2px] bg-low-contrast-text dark:bg-d-low-contrast-text"></div>
                        <p class=" translate-y-[2px]">{{ 2 * result.a }}</p>
                      </div>
                      <div v-else>
                        <span class="font-bold">{{ result.x2 }}</span>
                      </div>
                    </div>




                  </div>

                  <!-- <div class="text-lg text-low-contrast-text dark:text-d-low-contrast-text">
                    x<sub>1</sub> = {{ result.x1 }}<br />
                    x<sub>2</sub> = {{ result.x2 }}
                  </div> -->
                </div>
                <div v-else>
                  <div class="flex flex-row items-center gap-1 text-lg text-low-contrast-text dark:text-d-low-contrast-text">
                    <p>x = </p>
                    <div v-if="result.irreducible_x1" class="flex flex-col items-center justify-center font-bold">
                      <p class=" translate-y-[2px]">{{ result.x1_numerator }}</p>
                      <div class=" h-[2px] w-full translate-y-[2px] bg-low-contrast-text dark:bg-d-low-contrast-text"></div>
                      <p class=" translate-y-[2px]">{{ result.x1_denominator }}</p>
                    </div>
                    <div v-else>
                      <span class="font-bold">{{ result.x1 }}</span>
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <!-- Degree > 2 -->
            <div v-if="result.degree > 2"
              class="rounded-md border-l-4 border-accent-color bg-gray-50 p-4 shadow-md dark:border-d-accent-color dark:bg-gray-800">
              <p class="text-lg text-low-contrast-text dark:text-d-low-contrast-text">
                The equation has a degree higher than 2 and cannot be solved by this tool.
              </p>
            </div>
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


// DEGREES 0
// result.value = { 'degree': 0, 'equation': '3 = 0', 'has_solution': false }
// result.value = { 'degree': 0, 'equation': '3 = 0', 'has_solution': true }


// DEGREES 1
// result.value = {'a': 4,
//  'b': 1,
//  'degree': 1,
//  'equation': '4 * X + 1 = 0',
//  'has_solution': false,
//  'irreducible': false,
// //  'x': -0.25,
//  'x': -0.25,
// }
// result.value = {'a': 4,
//  'b': 1,
//  'degree': 1,
//  'equation': '4 * X + 1 = 0',
//  'has_solution': true,
//  'irreducible': false,
// //  'x': -0.25,
//  'x': -0.25,
// }
// result.value = {'a': 4,
//  'b': 1,
//  'degree': 1,
//  'equation': '4 * X + 1 = 0',
//  'has_solution': true,
//  'irreducible': true,
// //  'x': -0.25,
//  'x': -0.25,
// }


// DEGREES 2
// result.value = {'a': 3,
//  'b': -5,
//  'c': 2,
//  'degree': 2,
//  'delta': -1,
//  'equation': '3 * X^2 - 5 * X + 2 = 0',
//  'has_solution': false,
//  'irreducible_x1': true,
//  'x1_numerator': 12,
//  'x1_denominator': 8,
//  'irreducible_x2': false,
//  'x2_numerator': 12,
//  'x2_denominator': 8,
//  'x1': 0.6666666666666666,
//  'x2': 1}

// result.value = {'a': 3,
//  'b': -5,
//  'c': 2,
//  'degree': 2,
//  'delta': 0,
//  'equation': '3 * X^2 - 5 * X + 2 = 0',
//  'has_solution': true,
//  'irreducible_x1': true,
//  'x1_numerator': 12,
//  'x1_denominator': 8,
//  'irreducible_x2': false,
//  'x2_numerator': 12,
//  'x2_denominator': 8,
//  'x1': 0.6666666666666666,
//  'x2': 1}

// result.value = {'a': 3,
//  'b': -5,
//  'c': 2,
//  'degree': 2,
//  'delta': 0,
//  'equation': '3 * X^2 - 5 * X + 2 = 0',
//  'has_solution': true,
//  'irreducible_x1': true,
//  'x1_numerator': 12,
//  'x1_denominator': 8,
//  'irreducible_x2': false,
//  'x2_numerator': 12,
//  'x2_denominator': 8,
//  'x1': 0.6666666666666666,
//  'x2': 1}


// result.value = {'a': 3,
//  'b': -5,
//  'c': 2,
//  'degree': 2,
//  'delta': 2,
//  'equation': '3 * X^2 - 5 * X + 2 = 0',
//  'has_solution': true,
//  'irreducible_x1': true,
//  'x1_numerator': 12,
//  'x1_denominator': 8,
//  'irreducible_x2': false,
//  'x2_numerator': 12,
//  'x2_denominator': 8,
//  'x1': 0.6666666666666666,
//  'x2': 1}

// result.value = {'a': 3,
//  'b': -5,
//  'c': 2,
//  'degree': 2,
//  'delta': 2,
//  'equation': '3 * X^2 - 5 * X + 2 = 0',
//  'has_solution': true,
//  'irreducible_x1': false,
//  'x1_numerator': 12,
//  'x1_denominator': 8,
//  'irreducible_x2': false,
//  'x2_numerator': 12,
//  'x2_denominator': 8,
//  'x1': 0.6666666666666666,
//  'x2': 1}

// DEGREES > 2
// result.value = {'a': 3,
//  'b': -5,
//  'c': 2,
//  'degree': 5,
//  'delta': 2,
//  'equation': '3 * X^2 - 5 * X + 2 = 0',
//  'has_solution': true,
//  'irreducible_x1': false,
//  'x1_numerator': 12,
//  'x1_denominator': 8,
//  'irreducible_x2': false,
//  'x2_numerator': 12,
//  'x2_denominator': 8,
//  'x1': 0.6666666666666666,
//  'x2': 1}


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
      const data = await response.json();
      if (data.detail) {
        throw new Error(data.detail);
      } else {
        throw new Error;
      }
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
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s;
}

.fade-enter,
.fade-leave-to

/* .fade-leave-active in <2.1.8 */
  {
  opacity: 0;
}

/* Loading spinner styles */
.animate-spin {
  animation: spin 2s linear infinite;
}

@keyframes spin {
  0% {
    transform: rotate(0deg);
  }

  100% {
    transform: rotate(360deg);
  }
}
</style>
