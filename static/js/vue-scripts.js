console.log('happiness is key')

var tweets_url = document.querySelector('#add-tweet-url').getAttribute('data-add-tweet-url')

const app = Vue.createApp({
  delimiters: ["[[", "]]"],
  data() {
    return {
      all_tweets: [],
      form: {
        tweet_author: '',
        tweet: ''
      }
    }
  },

  created() {
    axios.get(tweets_url)
      .then(response => {this.all_tweets = response.data})
      .catch(errors => console.log(errors))
  },
  
  
  methods: {
    sortorder(event){
      var sortby = event.target.getAttribute('data-sortby');
      axios.get(tweets_url + '?sortby=' + sortby)
        .then(response => {this.all_tweets = response.data})
        .catch(errors => console.log(errors))
    },

    submitform(event) {
      var csrfmiddlewaretoken = document.getElementById('tweet-form').querySelector("input[name=csrfmiddlewaretoken]").value
      axios({
        method: 'post',
        url: tweets_url,
        data: {
          tweet_author: this.form.tweet_author,
          tweet: this.form.tweet
        },
        headers: {'X-CSRFToken': csrfmiddlewaretoken}
      })
      .then(response => {
        this.form.tweet_author = ''
        this.form.tweet = ''
        event.target.reset()
        this.all_tweets = response.data})
      .catch(errors => console.log(errors))
    },
  }
});




app.mount('#app')