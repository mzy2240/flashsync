<template>
  <n-input
    v-model="value"
    type="text"
    :placeholder="placeholder"
    :data-streamsync-id="componentId"
    v-show="!isPlaceholder"
  />
</template>

<script>
import { defineComponent, ref } from "vue";

export default defineComponent({
  setup() {
    return {
      value: ref(null),
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
    this.placeholder = this.streamsync.getContentValue(this.componentId, "placeholder");
    this.streamsync.addEventListeners(this.componentId, this.$el);
  },
  computed: {
    isPlaceholder: function () {
      return this.streamsync.components[this.componentId].placeholder;
    },
  },
});
</script>