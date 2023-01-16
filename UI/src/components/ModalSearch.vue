<template>
<div class="Popup">
  <div class="popup-inner">
    <slot/>
    <div>
    <input class="searchInput">
      &nbsp
      &nbsp
      <button class="searchButton">TIM KIEM</button>
     <br/>
      <br/>
      <input type="file" id="img" name="img" accept="image/*">
      <br/>
      <br/>
    </div>
    <br/>
    <button class="popup-close" @click="showModal()">
      Close
    </button>
  </div>
</div>
</template>

<script>
export default {
  name: 'ModalSearch',
  props: ['showModal']
}
</script>

<style scoped>
.Popup {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  z-index: 99;
  background-color: rgba(0, 0, 0, 0.2);

  display: flex;
  align-items: center;
  justify-content: center;
}
  .popup-inner {
    background: #EABE12;
    padding: 32px;
    width: 800px;
    border-radius: 15px;
  }
  .searchButton{
    padding: 15px 25px;
    box-shadow: 0 9px #999;
    border: none;
    border-radius: 15px;
  }
  .popup-close {
    padding: 15px 20px;
    box-shadow: 0 9px #999;
    border: none;
    border-radius: 15px;
  }
  .searchInput{
    width: 400px;
    height: 50px;
    border-radius: 15px;
  }
  .searchButton:hover {background-color: #3e8e41}
  .popup-close:hover {background-color: #dcbba8}
</style>
