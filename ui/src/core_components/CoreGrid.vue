<template>
  <n-config-provider :theme="theme.theme">
    <div
      class="component"
      :data-streamsync-id="componentId"
      v-show="!isPlaceholder"
    >
      <n-grid :cols="cols" x-gap="12">
        <n-gi v-for="i in cols" :key="i">
          <div
            v-for="n in volume[i - 1]"
            :key="`${n - 1}`"
            v-bind:id="`${componentId}-${i - 1}-${n - 1}`"
          ></div>
        </n-gi>
      </n-grid>
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
    cols: function () {
      return this.streamsync.getContentValue(this.componentId, "cols");
    },
    isPlaceholder: function () {
      return this.streamsync.components[this.componentId].placeholder;
    },
  },
});
</script>

<style>
</style>
