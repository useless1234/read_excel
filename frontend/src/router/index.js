import Vue from 'vue'
import Router from 'vue-router'
import uploadExcel from '@/components/uploadExcel'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'uploadExcel',
      component: uploadExcel
    }
  ]
})
