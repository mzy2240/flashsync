<template>
  <!-- <teleport :to="`#g${to}-${col}`" :disabled="to == null" v-if="isMounted"> -->
    <div
      class="CoreText component"
      :data-streamsync-id="componentId"
      v-show="!isPlaceholder"
    >
      <slot>{{ text }}</slot>
    </div>
  <!-- </teleport> -->
</template>

<script>
export default {
  inject: ["streamsync"],
  props: {
    componentId: String,
    to: String,
    col: Number,
  },
  data: function () {
    return {
      isMounted: false,
    };
  },
  mounted: function () {
    this.streamsync.addEventListeners(this.componentId, this.$el);
  },
  computed: {
    text: function () {
      let content = this.streamsync.getContentValue(this.componentId, "text");
      console.log(content)
      return content;
    },
    isPlaceholder: function () {
      let show = this.streamsync.components[this.componentId].placeholder;
      console.log(show)
      return show;
    },
  },
};
</script>

<style>
/* .CoreText {
  font-size: 0.8rem;
  white-space: pre-wrap;
} */
</style>
