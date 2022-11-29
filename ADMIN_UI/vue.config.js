const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  devServer: {
    host: 'fruitadmin.hufi.local',
    allowedHosts: "all",
   },
  transpileDependencies: true,
  lintOnSave: false,
})
