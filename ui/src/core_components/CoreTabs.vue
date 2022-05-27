<template>
  <n-config-provider :theme="theme.theme">
    <div
      class="component"
      :data-streamsync-id="componentId"
      v-show="!isPlaceholder"
    >
      <n-tabs type="line" animated>
        <n-tab-pane v-for="(item, index) in panels" :key="item" :name="item" :tab="item">
          <div
            v-for="n in volume[index]"
            :key="`${n - 1}`"
            v-bind:id="`${componentId}-${item}-${n - 1}`"
          ></div>
        </n-tab-pane>
      </n-tabs>
    </div>
  </n-config-provider>
</template>

<script>
import { defineComponent } from "vue";
import { useThemeStore } from "@/stores/theme";

export default defineComponent({
  inject: ["streamsync"],
  setup() {
    const theme = useThemeStore();
    return {
      theme,
    };
  },
  props: {
    componentId: String,
  },
  data: function () {
    return {
      volume: [],
    };
  },
  created() {
    this.volume = this.streamsync.components[this.componentId].volume;
  },
  mounted: function () {
    this.streamsync.addEventListeners(this.componentId, this.$el);
  },
  computed: {
    panels: function () {
      return this.streamsync.getContentValue(this.componentId, "panels");
    },
    isPlaceholder: function () {
      return this.streamsync.components[this.componentId].placeholder;
    },
  },
});
</script>

<style>
</style>
