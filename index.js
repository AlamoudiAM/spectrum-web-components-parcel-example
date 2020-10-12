import '@spectrum-web-components/theme/sp-theme.js';
import '@spectrum-web-components/theme/src/themes.js';
import '@spectrum-web-components/button/sp-button.js';
import '@spectrum-web-components/button/sp-clear-button.js';

import Vue from 'vue';
import { Button } from 'ant-design-vue';
import 'ant-design-vue/dist/antd.css';

Vue.use(Button);

var app = new Vue({
    el: '#app',
    data: {
        message: 'Hello Vue!'
    },
    components: { Button }
});