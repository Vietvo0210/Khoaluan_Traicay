const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  devServer: {
    host: 'hufifruit.kltn.local',
    allowedHosts: "all",
    host: '10.1.1.1'
   },
  transpileDependencies: true,
  lintOnSave: false,
})
