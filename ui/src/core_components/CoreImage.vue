<template>
  <!-- <n-button :data-streamsync-id="componentId" v-show="!isPlaceholder" text-color="white">
    {{ text }}
  </n-button> -->
  <n-image
    :data-streamsync-id="componentId"
    v-if="url"
    v-show="!isPlaceholder"
    :width="width"
    :src="url"
  />
  <n-image
    v-else
    :data-streamsync-id="componentId"
    v-show="!isPlaceholder"
    :width="width"
    :src="image"
  />
</template>

<script>
export default {
  inject: ["streamsync"],
  props: {
    componentId: String,
  },
  data: function () {
    return {
      url: null,
      image: null,
      width: 600
    };
  },
  //   created: function () {
  //     this.url = this.streamsync.getContentValue(this.componentId, "url");
  //   },
  mounted: function () {
    this.streamsync.addEventListeners(this.componentId, this.$el);
    this.width = this.streamsync.getRawValue(this.componentId, "width");
    this.url = this.streamsync.getRawValue(this.componentId, "url");
    if (this.url == null) {
      const image = this.streamsync.getRawValue(this.componentId, "data");
      this.image = image;
    }
  },
  computed: {
    isPlaceholder: function () {
      return this.streamsync.components[this.componentId].placeholder;
    },
  },
};
</script>

<style scoped>

</style>