new Vue({
    el: '#app',
    vuetify: new Vuetify(),
    data: {
        // auth
        icons: [
            {
                icon: 'mdi-facebook',
                href: 'https://www.facebook.com/mangoconsultant/'
            },
            {
                icon: 'mdi-twitter',
                href: ''
            },
            {
                icon: 'mdi-linkedin',
                href: ''
            },
            {
                icon: 'mdi-instagram',
                href: 'https://www.instagram.com/mangoconsultant/'
            },
        ],
        userAuth: {
            name: '',
            picture: '',
            email: '',
            uid: '',
        },
        spinAuth: false,
        notify_today: [],
        selectedNotify: 0,
        navigatorAppbar: false,
        selectedList: 1,
        itemsAppbar: [
            {text: 'Mango', icon: 'mdi-database'},
            {text: 'Intents', icon: 'mdi-account'},
        ],
        loaderSpin: true,
        loaderData: false,
    },
    beforeCreate() {
        const path = '/secure/read'
        axios.get(path)
            .then((res) => {
                this.loaderSpin = false
                this.loaderData = true
                let user = this.userAuth
                user.name = res.data.name
                user.picture = res.data.picture
                user.email = res.data.email
                user.uid = res.data.uid
            })
            .catch((err) => {
                console.error(err)
            })
    },
    computed: {
        datetimeNow() {
            const today = new Date();
            return today.getDate() + '/' + (today.getMonth() + 1) + '/' + today.getFullYear();
        },
    },
    methods: {
        logout() {
            return window.location = '/secure/logout'
        },
    },
    delimiters: ["[[", "]]"],
})