import { createApp } from "vue"
import naive from 'naive-ui'
import App from "./App.vue"
import streamsync from "./streamsync.js"

const app = createApp(App);
app.use(naive)

app.provide("streamsync", streamsync);

streamsync.init().then(() => {
    streamsync.startSync();
    app.mount("#app");
});