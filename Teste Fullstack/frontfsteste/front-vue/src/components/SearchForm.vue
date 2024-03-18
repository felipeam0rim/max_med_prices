<template>
  <form>
    <div class="search">
      <input type="text" placeholder="Digite para procurar" />
      <button type="button" class="search-button">Procurar</button>
      <button type="button" class="filter-button">Filtrar por:</button>
    </div>
  </form>
</template>

<script setup></script>

<style>
.search {
  height: 50px;
  margin-block: 50px;
  width: 100%;
  display: flex;
  justify-content: center;
}
.search-button {
  border-top-right-radius: 8px;
  border-bottom-right-radius: 8px;
  margin-right: 5px;
}
.filter-button {
  border-radius: 8px;
}
input {
  border-top-left-radius: 8px;
  border-bottom-left-radius: 8px;
}
</style>
