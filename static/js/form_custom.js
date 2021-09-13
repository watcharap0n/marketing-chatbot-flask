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
            {text: 'Dashboard', icon: 'mdi-monitor-dashboard'},
            {text: 'Intents', icon: 'mdi-account'},
        ],
        loaderSpin: true,
        loaderData: false,
        // end auth
        validOther: [v => !!v || 'กรุณากรอกข้อมูลให้ครบถ้วน'],
        validCombobox: [v => (v && v.length === 0) || 'กรุณาใส่ผลิตภัณฑ์อย่างน้อย 1 อย่าง'],
        valid: false,
        selectedProduct: '',
        selectedOther: '',
        form: {
            id: '',
            name: '',
            company: '',
            email: '',
            tel: '',
            other: '',
            message: '',
            channel: '',
            product: '',
            type: '',
            token_liff: '',
            itemProducts: [],
            itemOthers: []
        },
        spinData: false
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
    mounted() {
        this.form.id = this.$refs.formId.value
        this.getForm()
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
       redirectPage(item) {
            console.log(item)
            if (item.text === 'Mango')
                window.location = '/'
            if (item.text === 'Intents')
                window.location = '/intents'
            if (item.text === 'Dashboard')
                window.location = '/dashboard'
        },
        getForm() {
            const path = `/api/form/custom/get?id=${this.form.id}`
            axios.get(path)
                .then((res) => {
                    this.form = res.data.item
                    this.spinData = true
                })
                .catch((err) => {
                    console.error(err);
                })
        },
        updateProduct() {
            this.spinData = false
            const path = `/api/form/custom/update/product/${this.form.id}`
            axios.put(path, this.form)
                .then((res) => {
                    console.log(res.data)
                    this.product = ''
                    this.spinData = true
                })
                .catch((err) => {
                    console.log(err)
                })

        },
        addProduct(data) {
            if (this.selectedProduct || this.selectedOther) {
                if (data.key === 'product') {
                    this.form.itemProducts.push(this.selectedProduct)
                    this.selectedProduct = ''
                    this.updateProduct()
                } else if (data.key === 'other') {
                    this.form.itemOthers.push(this.selectedOther)
                    this.selectedOther = ''
                    this.updateProduct()
                }
            } else {
                console.log(null)
            }
        },
        deleteProduct(data) {
            if (data.key === 'product') {
                this.form.itemProducts.splice(this.form.itemProducts.indexOf(data.item), 1)
                this.updateProduct()
            } else if (data.key === 'other') {
                this.form.itemOthers.splice(this.form.itemOthers.indexOf(data.item), 1)
                this.updateProduct()
            }
        },
    },
    delimiters: ["[[", "]]"],
})