<template>

<v-container fluid>
  <v-layout column text-xs-center>
    <v-flex>

      <v-list dark>
      
        <template v-for="(item, index) in items">

        <v-list-tile
          :key="index"
          @click=""
          ripple
        >

          <v-list-tile-content>
            <v-list-tile-title>{{ item.title }}</v-list-tile-title>
          </v-list-tile-content>

        </v-list-tile>
        <v-divider v-if="index + 1 < items.length" :key="`divider-${index}`"></v-divider>
        </template>
      </v-list>

    </v-flex>
  </v-layout>

  <v-speed-dial
    bottom
    right
    fixed
  >
    <v-btn
      slot="activator"
      color="blue darken-2"
      dark
      fab
    >
      <v-icon>account_circle</v-icon>
      <v-icon>close</v-icon>
    </v-btn>

    <v-tooltip left>
        <v-btn fab dark small color="indigo" slot="activator" @click="dialog=!dialog">
          <v-icon>edit</v-icon>
        </v-btn>
        <span>Add Note</span>
    </v-tooltip>    
    <v-tooltip left>
        <v-btn fab dark small color="yellow" slot="activator" @click="dialog=!dialog">
          <v-icon>edit</v-icon>
        </v-btn>
        <span>Add Log Entry</span>
    </v-tooltip>    
    <v-tooltip left>
      <v-btn fab dark small color="green" slot="activator" @click="dialog=!dialog">
        <v-icon>add</v-icon>
      </v-btn>
      <span>Add and Activate New Task</span>
    </v-tooltip>
    <v-tooltip left>
      <v-btn fab dark small color="gray" slot="activator" @click="dialog=!dialog">
        <v-icon>add</v-icon>
      </v-btn>
      <span>Add New Inactive Task</span>
    </v-tooltip>    
    <v-tooltip left>
      <v-btn fab dark small color="red" slot="activator">
        <v-icon>delete</v-icon>
      </v-btn>
      <span>Delete Task</span>
    </v-tooltip>  

  </v-speed-dial>

  <v-dialog v-model="dialog" width="800px">
    <v-card>
      <v-card-title class="grey lighten-4 py-4 title">Add New</v-card-title>
      <v-container>
        <v-textarea v-model="message" full-width></v-textarea>
      </v-container>
      <v-divider></v-divider>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn flat color="primary" @click="dialog = false">Cancel</v-btn>
        <v-btn flat @click="dialog = false">Save</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>

</v-container>

</template>

<script>
  export default {
    data () {
      return {
        items: [
          {title: 'hello'},
          {title: 'world'},
          {title: 'this is another task'}
        ],
        dialog: 'false',
        message: ''
      }
    },

    methods: {

    }
  }
</script>