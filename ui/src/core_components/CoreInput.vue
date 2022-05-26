<template>
  <n-config-provider :theme="theme.theme">
    <n-input
      v-model="value"
      type="text"
      :placeholder="placeholder"
      :data-streamsync-id="componentId"
      v-show="!isPlaceholder"
    />
  </n-config-provider>
</template>

<script>
import { defineComponent, ref } from "vue";
import { useThemeStore } from "@/stores/theme";

export default defineComponent({
  setup() {
    const theme = useThemeStore();
    return {
      value: ref(null),
      theme,
    };
  },
  inject: ["streamsync"],
  props: {
    componentId: String,
  },
  data: function () {
    return {
      placeholder: null,
    };
  },
  mounted: function () {
    this.placeholder = this.streamsync.getContentValue(
      this.componentId,
      "placeholder"
    );
    this.streamsync.addEventListeners(this.componentId, this.$el);
  },
  computed: {
    isPlaceholder: function () {
      return this.streamsync.components[this.componentId].placeholder;
    },
  },
});
</script>