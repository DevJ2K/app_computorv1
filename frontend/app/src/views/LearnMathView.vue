<template>
  <main class="container mx-auto my-12 px-4 text-high-contrast-text dark:text-d-high-contrast-text md:px-8 lg:px-16">
    <!-- Titre Principal de la Page -->
    <div class="flex w-full items-center justify-center">
      <h1 class="border-b-2 border-accent-color pb-2 text-4xl font-extrabold text-high-contrast-text dark:border-d-accent-color dark:text-d-high-contrast-text">Learn the Math</h1>
    </div>

    <!-- Introduction -->
    <section class="mb-12">
      <h2 class="mb-4 text-2xl font-semibold text-high-contrast-text dark:text-d-high-contrast-text">Introduction</h2>
      <p class="text-lg text-low-contrast-text dark:text-d-low-contrast-text">
        Understanding the basics of algebra and equations is essential to solving problems with Computorv1. In this section, we will cover key concepts such as quadratic equations and linear equations, along with methods to solve them.
      </p>
    </section>

    <!-- Qu'est-ce qu'une équation du second degré ? -->
    <section class="mb-12">
      <h2 class="mb-4 text-2xl font-semibold text-high-contrast-text dark:text-d-high-contrast-text">What is a Quadratic Equation?</h2>
      <p class="mb-4 text-lg text-low-contrast-text dark:text-d-low-contrast-text">
        A quadratic equation is a polynomial equation of the second degree. It is generally represented in the form:
        <span class="font-bold">ax<sup>2</sup> + bx + c = 0</span>, where <span class="font-bold">a</span>, <span class="font-bold">b</span>, and <span class="font-bold">c</span> are constants, and <span class="font-bold">a ≠ 0</span>.
      </p>
      <p class="mb-4 text-lg text-low-contrast-text dark:text-d-low-contrast-text">
        Quadratic equations are called "quadratic" because "quad" refers to the square (x<sup>2</sup>) term. They have a wide range of applications in physics, engineering, and other fields where the relationship between variables is non-linear.
      </p>

      <!-- Discriminant Section -->
      <p class="mb-4 text-lg text-low-contrast-text dark:text-d-low-contrast-text">
        The solutions of a quadratic equation depend on the value of the discriminant, denoted as <span class="font-bold">Δ</span> (delta). The discriminant is calculated using the formula:
        <span class="font-bold">Δ = b<sup>2</sup> - 4ac</span>.
      </p>
      <ul class="mb-4 list-inside list-disc text-lg text-low-contrast-text dark:text-d-low-contrast-text">
        <li><span class="font-bold">If Δ > 0</span>: The equation has two distinct real solutions.</li>
        <li><span class="font-bold">If Δ = 0</span>: The equation has exactly one real solution (a repeated root).</li>
        <!-- eslint-disable-next-line vue/no-parsing-error -->
        <li><span class="font-bold">If Δ < 0</span>: The equation has no real solutions (the solutions are complex or imaginary).</li>
      </ul>

      <!-- Exemples et illustration -->
      <div class="rounded-md border-l-4 border-accent-color bg-gray-50 p-4 shadow-md dark:border-d-accent-color dark:bg-gray-800">
        <h3 class="mb-2 text-xl font-semibold text-high-contrast-text dark:text-d-high-contrast-text">Example of a Quadratic Equation:</h3>
        <p class="text-lg text-high-contrast-text dark:text-d-high-contrast-text"><span class="font-bold">2x<sup>2</sup> - 4x - 6 = 0</span></p>
      </div>
    </section>

    <!-- Comment résoudre une équation du second degré -->
    <section class="mb-12">
      <h2 class="mb-4 text-2xl font-semibold text-high-contrast-text dark:text-d-high-contrast-text">How to Solve a Quadratic Equation?</h2>
      <p class="mb-4 text-lg text-low-contrast-text dark:text-d-low-contrast-text">
        There are several methods to solve a quadratic equation, including factoring, completing the square, and using the quadratic formula:
      </p>

      <!-- Factoring -->
      <div class="mb-6">
        <h3 class="mb-2 text-xl font-semibold text-high-contrast-text dark:text-d-high-contrast-text">1. Factoring</h3>
        <p class="text-lg text-low-contrast-text dark:text-d-low-contrast-text">
          If the quadratic equation can be factored, it can be written as the product of two binomials set to zero. For example, for the equation x<sup>2</sup> - 5x + 6 = 0, it can be factored into (x - 2)(x - 3) = 0. Setting each factor to zero gives the solutions: x = 2 and x = 3.
        </p>
      </div>

      <!-- Completing the Square -->
      <div class="mb-6">
        <h3 class="mb-2 text-xl font-semibold text-high-contrast-text dark:text-d-high-contrast-text">2. Completing the Square</h3>
        <p class="text-lg text-low-contrast-text dark:text-d-low-contrast-text">
          This method involves rearranging the equation into a perfect square trinomial. For the equation x<sup>2</sup> + 6x + 8 = 0, rearrange to form (x + 3)<sup>2</sup> - 1 = 0. Solving for x gives the solution x = -2 and x = -4.
        </p>
      </div>

      <!-- Quadratic Formula -->
      <div class="mb-6">
        <h3 class="mb-2 text-xl font-semibold text-high-contrast-text dark:text-d-high-contrast-text">3. Using the Quadratic Formula</h3>
        <p class="text-lg text-low-contrast-text dark:text-d-low-contrast-text">
          The quadratic formula is a universal method for solving any quadratic equation:
          <span class="my-4 block text-xl font-bold">
            x = <span class="text-2xl">(-b ± √(b<sup>2</sup> - 4ac))</span> / <span class="text-2xl">2a</span>
          </span>
          Using this formula, you can find the solutions of any quadratic equation by substituting the values of <span class="font-bold">a</span>, <span class="font-bold">b</span>, and <span class="font-bold">c</span>.
        </p>
      </div>
    </section>

    <!-- Qu'est-ce qu'une fonction affine ? -->
    <section class="mb-12">
      <h2 class="mb-4 text-2xl font-semibold text-high-contrast-text dark:text-d-high-contrast-text">What is a Linear Equation?</h2>
      <p class="mb-4 text-lg text-low-contrast-text dark:text-d-low-contrast-text">
        A linear equation, or affine function, is an equation of the first degree. It is represented as:
        <span class="font-bold">ax + b = 0</span>, where <span class="font-bold">a</span> and <span class="font-bold">b</span> are constants, and <span class="font-bold">a ≠ 0</span>.
      </p>
      <p class="text-lg text-low-contrast-text dark:text-d-low-contrast-text">
        Linear equations describe straight-line relationships and have only one solution unless the equation is inconsistent (which would imply no solution).
      </p>
      <!-- Exemples et illustration -->
      <div class="rounded-md border-l-4 border-accent-color bg-gray-50 p-4 shadow-md dark:border-d-accent-color dark:bg-gray-800">
        <h3 class="mb-2 text-xl font-semibold text-high-contrast-text dark:text-d-high-contrast-text">Example of a Linear Equation:</h3>
        <p class="text-lg text-high-contrast-text dark:text-d-high-contrast-text"><span class="font-bold">3x + 5 = 0</span></p>
        <p class="text-lg text-high-contrast-text dark:text-d-high-contrast-text">Solution: x = -5/3</p>
      </div>
    </section>

    <!-- Comment résoudre une fonction affine -->
    <section class="mb-12">
      <h2 class="mb-4 text-2xl font-semibold text-high-contrast-text dark:text-d-high-contrast-text">How to Solve a Linear Equation?</h2>
      <p class="mb-4 text-lg text-low-contrast-text dark:text-d-low-contrast-text">
        Solving a linear equation involves isolating the variable. Rearrange the equation to get the variable on one side and the constants on the other:
      </p>
      <div class="rounded-md border-l-4 border-accent-color bg-gray-50 p-4 shadow-md dark:border-d-accent-color dark:bg-gray-800">
        <h3 class="mb-2 text-xl font-semibold text-high-contrast-text dark:text-d-high-contrast-text">Example:</h3>
        <p class="text-lg text-low-contrast-text dark:text-d-low-contrast-text">Given the equation 3x + 6 = 0, subtract 6 from both sides: 3x = -6, then divide by 3: x = -2.</p>
      </div>
    </section>

    <!-- Conclusion -->
    <section class="mb-12">
      <h2 class="mb-4 text-2xl font-semibold text-high-contrast-text dark:text-d-high-contrast-text">Conclusion</h2>
      <p class="text-lg text-low-contrast-text dark:text-d-low-contrast-text">
        Understanding and solving both quadratic and linear equations are fundamental skills in mathematics. With Computorv1, you can practice and hone these skills, providing a strong foundation for tackling more complex problems in the future.
      </p>
    </section>
  </main>
</template>

<script setup lang="ts">
</script>
