<template>
  <div class="wrapper">
    <form @submit.prevent="submitForm">
      <div class="search">
        <input type="text" placeholder="Digite para procurar" v-model="query" />
        <button type="button" class="search-button">Procurar</button>
        <button type="button" class="filter-button">Filtrar por:</button>
      </div>
    </form>
    <div class="table">
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>Substância</th>
            <th>CNPJ</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="med_profile in med_profiles">
            <td>{{ med_profile.profile_id }}</td>
            <td>{{ med_profile.substancia }}</td>
            <td>{{ med_profile.cnpj }}</td>
          </tr>
        </tbody>
      </table>
    </div>
    <div class="pagination">
      <button v-if="showPrevButton" @click="loadPrev()">Página Anterior</button>
      <button v-if="showNextButton" @click="loadNext()">Próxima Página</button>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "MedProfiles",
  data() {
    return {
      med_profiles: [],
      showNextButton: false,
      showPrevButton: false,
      currentPage: 1,
      // query: "",
    };
  },
  mounted() {
    this.getMedProfiles();
  },
  methods: {
    loadNext() {
      this.currentPage += 1;
      this.getMedProfiles();
    },
    loadPrev() {
      this.currentPage -= 1;
      this.getMedProfiles();
    },
    async getMedProfiles() {
      this.showNextButton = false;
      this.showPrevButton = false;

      await axios
        .get(
          // &search=${this.query}
          `http://127.0.0.1:8000/med_profiles/?page=${this.currentPage}`
        )
        .then((response) => {
          console.log(response.data);
          this.med_profiles = response.data.results;
          if (response.data.next) {
            this.showNextButton = true;
          }
          if (response.data.previous) {
            this.showPrevButton = true;
          }
        });
    },
    // submitForm() {
    //   console.log(this.query);
    //   this.getMedProfiles();
    // },
  },
};
</script>

<style>
.wrapper {
  display: block;
  justify-content: center;
}

.table {
  display: flex;
  justify-content: center;
  margin-top: 40px;
  text-align: center;
}
.pagination {
  display: flex;
  justify-content: space-evenly;
}
.search {
  height: 50px;
  margin-top: 50px;
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
table {
  border-collapse: collapse;
}
th,
td {
  border: 2px solid black;
  padding: 10px;
}
</style>
