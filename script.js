Vue.component('hash-tag', {
    props: ['id', 'tag', 'select_all'],
    template: `
        <div class="hashT" @click='$emit("add", tag[0])'>
            <input :checked='select_all' type="checkbox" :id="id">
            <label :for='id'>
                <span>#{{tag[0]}}</span>
            </label>
        </div>
    `
})




const app = new Vue({
    el: '#app',
    data: {
        search: '',
        hashtags: [],
        select_all: false,
        toCopy: '',
        text_button: 'copy all'
    },
    watch: {
        search: function () {
            if (this.search.trim().length >= 1) {
                axios.get('https://maiconctn.pythonanywhere.com/api/' + this.search).then(e => {
                    this.hashtags = (e.data)
                })
            }
        },

        select_all: function () {
            if (this.select_all){
                this.hashtags.forEach( e => {
                    this.toCopy += `#${e}, `
                });
            }else {
                this.toCopy = ''
            }
        }
    },

    methods: {
        serachBT: function () {
            if (this.search.trim().length >= 1) {    
                axios.get('https://maiconctn.pythonanywhere.com/api/' + this.search).then(e => {
                    this.hashtags = (e.data)
                })
            }
        },
        add: function (tag) {
            if (event.target.nodeName === 'INPUT') {
                if (event.target.checked){
                    this.toCopy += `#${tag}, `
                }else{
                    this.toCopy = this.toCopy.replace(`#${tag}, `, '')
                }
            }
        },

        copyAll: function () {
            let copy = document.querySelector('.copy')
            copy.select()
            navigator.clipboard.writeText(copy.value)
            alert('copied')
        }
    }
})