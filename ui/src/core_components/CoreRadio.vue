<template>
  <n-config-provider :theme="theme.theme">
    <n-radio-group
      v-model="value"
      name="radiogroup"
      :data-streamsync-id="componentId"
      v-show="!isPlaceholder"
    >
      <n-space>
        <n-radio v-for="item in opts" :value="item" :key="item">
          {{ item }}
        </n-radio>
      </n-space>
    </n-radio-group>
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
      value: ref(null),
      theme,
    };
  },
  props: {
    componentId: String,
  },
  data: function () {
    return {
      opts: [],
    };
  },
  created: function () {
    this.opts = this.streamsync.getContentValue(this.componentId, "options");
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