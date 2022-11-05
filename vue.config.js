const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  devServer: {
    host: 'hufifruit.kltn.local',
    allowedHosts: "all",
  },
  transpileDependencies: true,
  lintOnSave: false,
})
