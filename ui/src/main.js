import { createApp } from "vue"
import { createPinia } from 'pinia'
import App from "./App.vue"
import streamsync from "./streamsync.js"
import { useThemeStore } from '@/stores/theme'

const app = createApp(App);
app.use(createPinia())
const theme = useThemeStore()

app.provide("streamsync", streamsync);
app.provide("theme", theme);

streamsync.init().then(() => {
    streamsync.startSync();
    app.mount("#app");
});