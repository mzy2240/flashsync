<template>
  <teleport :to="to" v-if="isMounted && to !== null">
    <slot></slot>
  </teleport>
  <!-- <slot v-else></slot> -->
</template>

<script>
export default {
  name: "CustomTeleport",
  props: ["to"],
  data() {
    return { isMounted: false };
  },
  mounted() {
    this.isMounted = true;
  },
};
</script>