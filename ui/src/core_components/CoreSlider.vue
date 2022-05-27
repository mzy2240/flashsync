<template>
  <n-config-provider :theme="theme.theme">
    <n-slider
      :min="min"
      :max="max"
      v-model="value"
      @update:value="handleChange($event)"
      :data-streamsync-id="componentId"
      v-show="!isPlaceholder"
    />
  </n-config-provider>
</template>

<script>
import { useThemeStore } from "@/stores/theme";

export default {
  inject: ["streamsync"],
  setup() {
    const theme = useThemeStore();
    return {
      theme,
    };
  },
  //   emit: ["change"],
  data: function () {
    return {
      value: 0,
    };
  },
  props: {
    componentId: String,
  },
  mounted: function () {
    this.streamsync.addEventListeners(this.componentId, this.$el);
  },
  methods: {
    handleChange: function (value) {
      let event = {};
      event.type = "change";
      event.targetId = this.componentId;
      event.value = value;
      this.streamsync.forward(event, true);
    },
  },
  computed: {
    text: function () {
      return this.streamsync.getContentValue(this.componentId, "text");
    },
    min: function () {
      const v = this.streamsync.getContentValue(this.componentId, "min");
      if (v === null) return 0;
      return v;
    },
    max: function () {
      const v = this.streamsync.getContentValue(this.componentId, "max");
      if (v === null) return 0;
      return v;
    },
    isPlaceholder: function () {
      return this.streamsync.components[this.componentId].placeholder;
    },
  },
};
</script>

<style scoped>
.CoreSlider {
  display: flex;
  align-items: center;
}

.main {
  display: block;
  padding-top: 0.7rem;
  width: 30ch;
}

input {
  width: 100%;
  margin: 0;
}

.rangeLabelContainer {
  align-items: center;
  display: flex;
  justify-content: space-between;
  font-size: 0.7rem;
}

h2 {
  margin: 0;
}

.label {
  min-width: 32px;
  text-align: center;
  margin-left: 24px;
  padding: 16px;
  border-radius: 8px;
  background: var(--subtleHighlight);
}
</style>
