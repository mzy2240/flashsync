<template>
  <n-button :data-streamsync-id="componentId" v-show="!isPlaceholder">
    {{ text }}
  </n-button>
</template>

<script>
export default {
  inject: ["streamsync"],
  props: {
    componentId: String,
  },
  data: function () {
    return {
      text: "",
    };
  },
  created: function () {
    this.text = this.streamsync.getContentValue(this.componentId, "text");
  },
  mounted: function () {
    this.streamsync.addEventListeners(this.componentId, this.$el);
  },
  computed: {
    isPlaceholder: function () {
      return this.streamsync.components[this.componentId].placeholder;
    },
  },
};
</script>

<style>
button {
  font-size: 0.8rem;
  border-radius: 8px;
  border: 1px solid var(--separator);
  padding: 12px;
  background: white;
  display: block;
  cursor: pointer;
}

button:hover {
  border: 1px solid #35485f;
}
</style>
