<template>
  <div
    class="component"
    :data-streamsync-id="componentId"
    v-show="!isPlaceholder"
  >
    <n-config-provider :theme="theme.theme">
      <n-layout-sider
        collapse-mode="width"
        :collapsed-width="0"
        :width="240"
        :show-collapsed-content="false"
        show-trigger="arrow-circle"
        content-style="padding: 24px;"
        bordered
      >
        <div
          v-for="n in volume"
          :key="`${n - 1}`"
          v-bind:id="`${componentId}-${n - 1}`"
        ></div>
      </n-layout-sider>
    </n-config-provider>
  </div>
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
      volume: 0,
    };
  },
  created() {
    this.volume = this.streamsync.components[this.componentId].volume;
  },
  mounted: function () {
    this.streamsync.addEventListeners(this.componentId, this.$el);
  },
  computed: {
    isPlaceholder: function () {
      return this.streamsync.components[this.componentId].placeholder;
    },
  },
});
</script>

<style>
</style>
