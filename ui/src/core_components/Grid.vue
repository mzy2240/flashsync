<template>
  <n-config-provider :theme="darkTheme">
    <n-grid :cols="gridcols" x-gap="12">
      <n-gi v-for="i in gridcols" :key="i">
        <div v-bind:id="`grid-item-${i-1}`"></div>
      </n-gi>
    </n-grid>
  </n-config-provider>
</template>

<script>
import { defineComponent, createApp } from "vue";
import { darkTheme } from "naive-ui";
import templateMapping from "../templateMapping.js";
import streamsync from "../streamsync.js";

export default defineComponent({
  inject: ["streamsync"],
  setup() {
    return {
      darkTheme,
    };
  },
  props: {
    gridid: String,
    gridcols: Number,
    components: Array,
  },
  mounted: function () {
    this.components.forEach(([componentId, component]) => {
      this.renderComponent(componentId, component);
    });
  },
  computed: {},
  methods: {
    renderComponent: function (componentId, component) {
      const template = templateMapping[component.type];
      if (!template) return; // Unmapped type
      const wrapper = document.getElementById(`grid-item-${component.grididx}`);
      const subApp = createApp(template, {
        componentId,
        isPlaceholder: component.placeholder,
      });
      subApp.provide("streamsync", streamsync);
      subApp.mount(wrapper);
    },
  },
});
</script>

<style>
</style>
