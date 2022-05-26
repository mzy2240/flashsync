import { defineStore } from 'pinia'
import { ref } from "vue";
import { darkTheme } from "naive-ui";

export const useThemeStore = defineStore('theme', {
    state: () => {
        return { theme: ref(null) }
    },
    // could also be defined as
    // state: () => ({ count: 0 })
    actions: {
        changeTheme(theme) {
            if (theme === 'dark') {
                this.theme = darkTheme
            } else if (theme === 'light') {
                this.theme = null
            }
        }
    },
})