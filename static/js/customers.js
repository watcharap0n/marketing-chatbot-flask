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
            collection: '',
            _import: '',
        },
        spinAuth: false,
        notify_today: [],
        selectedNotify: 0,
        // Appbar
        navigatorAppbar: false,
        selectedList: 0,
        itemsAppbar: [
            {text: 'Mango', icon: 'mdi-database'},
            {text: 'Dashboard', icon: 'mdi-monitor-dashboard'},
            {text: 'Intents', icon: 'mdi-account'},
        ],

        loaderSpin: true,
        loaderData: false,
        //================================

        // datetime
        date: [],
        menu1: false,
        dialogDate: false,

        // excel
        dialogExcel: false,
        btnExcel: true,
        spinExcel: false,
        spinPreview: true,

        // table
        page: 1,
        hiddenAPI: true,
        navigation: [
            {
                header: 'ข้อมูลลูกค้า',
                href: 'customers',
                icon: 'mdi-account-supervisor-circle'
            },
            {
                header: 'นำเข้า',
                href: 'imports',
                icon: 'mdi-import'
            },
            {
                header: 'API',
                href: 'api',
                icon: 'mdi-api'
            }
        ],
        headers: [
            {
                text: 'แก้ไข/ลบ',
                value: 'actions',
                width: 120,
                sortable: false,
            },
            {
                text: 'แท็ก',
                value: 'tag',
                width: 140
            },
            {
                text: 'ผลิตภัณฑ์',
                value: 'product',
                align: 'start',
                width: 140
            },
            {
                text: 'อื่นๆ',
                value: 'other',
                align: "center",
                width: 140,
            },
            {
                text: 'ข้อมูลลูกค้า',
                value: 'name',
                align: 'center',
                width: 150,
            },
            {
                text: 'บริษัท',
                value: 'company',
                width: 140
            },
            {
                text: 'ข้อความ',
                value: 'message',
                width: 140
            },
            {
                text: 'ช่องทาง',
                value: 'channel',
                width: 140
            },
            {
                text: 'โปรไฟล์',
                value: 'profile',
                width: 140

            },
            {
                text: 'คนนำเข้า',
                value: 'username',
                width: 140
            },
            {
                text: 'วัน/เวลา',
                value: 'date',
                align: 'center',
                width: 140
            },

        ],
        editedItem: {
            id: '',
            person_id: '',
            tax_id: '',
            name: '',
            tag: [],
            product: '',
            email: '',
            email_private: '',
            profile: '',
            picture: '',
            userId: '',
            other: '',
            tel: '',
            company: '',
            channel: '',
            message: '',
            username: '',
            uid: '',
        },
        defaultItem: {
            id: '',
            person_id: '',
            tax_id: '',
            name: '',
            tag: [],
            product: '',
            email: '',
            email_private: '',
            profile: '',
            picture: '',
            userId: '',
            other: '',
            tel: '',
            company: '',
            channel: '',
            message: '',
            username: '',
            uid: '',
        },
        valid: true,
        search: '',
        transaction: [],
        selected: [],
        spinButton: true,
        imgError: false,
        spinTable: false,
        dialogCustomer: false,
        dialogDelete: false,
        editedIndex: -1,
        snackbar: false,
        btnImport: false,
        spinImport: false,
        timeout: 2000,
        colorSb: '',
        text: '',
        path: '',
        href: '',
        isProfile: false,
        selectedProduct: '',
        selectedChannel: '',
        selectedTag: '',
        products: [],
        channels: [],
        tags: [],
        productMango: ['RealEstate', 'Construction', 'BI Dashboard', 'Project Planning', 'CSM', 'QCM', 'Maintenance', 'Rental', 'MRP'],

        // tags
        itemsTag: [],
        searchTag: null,
        editingTag: null,
        colorsTag: 'pink',
        model: [],
        btnTag: false,
        btnDelete: false,
        spinDelete: true,
        spinTag: true,

        sheet: false,
        tiles: [
            {img: 'keep.png', title: 'Keep'},
            {img: 'inbox.png', title: 'Inbox'},
            {img: 'hangouts.png', title: 'Hangouts'},
            {img: 'messenger.png', title: 'Messenger'},
            {img: 'google.png', title: 'Google+'},
        ],


        // btn or table hidden
        btnHiddenAPI: true,
        btnAPI: false,

        // import excel
        dialogImportExcel: false,
        rulesImport: [
            value => !value || value.size < 2000000 || 'ขนาดไฟล์ควรน้อยกว่า 2 MB!',
        ],
        fileImportExcel: null,

        //Program RE
        accountRE: {},
        tokenRE: '',
        spinRE: true,
        btnRE: false,
        itemsRE: [],
        usersRE: [],
        itemsDuplicateRE: [],
        dialogDuplicateRE: false,
        dialogConfirmRE: false,
        dialogUpdateRE: false
    },


    watch: {
        date(val) {
            if (this.date.length > 0) {
                this.$refs.form.reset()
            }
        },
        model(val, prev) {
            if (val.length === prev.length) return
            this.model = val.map(v => {
                if (typeof v === 'string') {
                    v = {
                        text: v,
                        color: this.colorsTag
                    }
                    this.addTag(v)
                    this.nonce++
                }
                return v
            })
            if (this.model.length > 0 && this.selected.length > 0) {
                this.btnTag = true
            } else if (this.model.length === 0 || this.selected.length === 0) {
                this.btnTag = false
            }
        },
        selected() {
            if (this.selected.length > 0 && this.model.length > 0) {
                this.btnTag = true
            } else if (this.selected.length === 0 || this.model.length === 0) {
                this.btnTag = false
            }
            if (this.selected.length > 0 && this.page !== 2) {
                this.btnDelete = true
            } else if (this.selected.length === 0) {
                this.btnDelete = false
            }
        }

    },

    async mounted() {
        const path = '/secure/read'
        await axios.get(path)
            .then((res) => {
                this.loaderSpin = false
                this.loaderData = true
                let user = this.userAuth
                user.name = res.data.name
                user.picture = res.data.picture
                user.email = res.data.email
                user.uid = res.data.uid
                user.collection = res.data.collection
                user._import = res.data._import
            })
            .catch((err) => {
                console.error(err)
            })
        await this.APIImport();
        await this.getTags();
        await this.getUserRE();
    },
    computed: {
        datetimeNow() {
            const today = new Date();
            return today.getDate() + '/' + (today.getMonth() + 1) + '/' + today.getFullYear();
        },
        formTitle() {
            return this.editedIndex === -1 ? 'เพิ่มข้อมูล' : 'แก้ไขข้อมูล'
        },
        dateRangeText() {
            return this.date.join(' ~ ')
        },
    },
    methods: {
        // table
        async initialize() {
            this.spinTable = false
            const path = `/api/customer?collection=${this.userAuth.collection}`
            await axios.get(path)
                .then((res) => {
                    this.btnRE = false
                    this.btnHiddenAPI = true
                    this.btnAPI = true
                    this.spinTable = true;
                    this.transaction = res.data.transaction;
                    this.products = res.data.products
                    this.channels = res.data.channels
                    this.tags = res.data.tags
                    this.href = 'customer'
                    this.btnImport = false
                })
                .catch((err) => {
                    console.log(err)
                })
        },
        async APIImport() {
            this.spinTable = false
            const path = `/api/import?collection=${this.userAuth._import}`
            await axios.get(path)
                .then((res) => {
                    this.btnRE = false
                    this.btnAPI = false
                    this.btnHiddenAPI = true
                    this.spinTable = true;
                    this.notify_today = res.data.notify_today
                    this.transaction = res.data.transaction;
                    this.href = 'import'
                    this.btnImport = true
                })
                .catch((err) => {
                    console.log(err)
                })
        },

        // excel
        openDialog() {
            if (this.selected.length === 0) {
                this.btnExcel = false
            } else if (this.selected.length > 0) {
                this.btnExcel = true
                this.spinExcel = true
            }
        },
        submitExcel(selected) {
            this.btnExcel = true
            let data = {}
            let data_id = []
            selected.forEach((v) => {
                data_id.push(v.id)
            })
            data.id = data_id
            this.spinExcel = false
            if (this.href === 'customer') {
                data.collection = this.userAuth.collection
                this.exportExcel('/api/datafile/customer/excel', data)
            }
            if (this.href === 'import') {
                data.collection = this.userAuth._import
                this.exportExcel('/api/datafile/import/excel', data)
            }
        },
        async exportExcel(path, data) {
            await axios.post(path, data, {
                headers: {
                    'Content-Type': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
                    'Content-Disposition': "attachment; filename=customers.xlsx"
                },
                responseType: 'blob'
            })
                .then((res) => {
                    const blob = res.data;
                    const link = document.createElement("a");

                    link.href = URL.createObjectURL(blob);
                    link.download = 'customers.xlsx';
                    document.body.appendChild(link);
                    link.click();
                    document.body.removeChild(link);
                    this.spinExcel = true
                    this.dialogExcel = false
                })
                .catch((err) => {
                    this.spinExcel = true
                    console.error(err)
                })
        },

        // sorting
        tableSorting() {
            if (this.date.length === 0 && !this.selectedChannel && !this.selectedProduct && !this.selectedTag) {
                this.$refs.form.validate()
            } else {
                let dict = {
                    date: this.date,
                    channel: this.selectedChannel,
                    product: this.selectedProduct,
                    tag: [],
                }
                if (this.selectedTag) {
                    dict.tag = [this.selectedTag]
                }
                if (this.href === 'customer') {
                    dict.collection = this.userAuth.collection
                    this.sendSorting('/api/c/sorting', dict)
                    this.$refs.form.reset()
                }
                if (this.href === 'import') {
                    dict.collection = this.userAuth._import
                    this.sendSorting('/api/m/sorting', dict)
                    this.$refs.form.reset()
                }
                this.$refs.form.reset()
                this.dialogDate = false
            }
        },
        sortingOnclick(data) {
            if (this.page !== 2) {
                let dict = {
                    date: [],
                    channel: null,
                    product: null,
                    tag: null,
                }
                if (data.channel) {
                    dict.channel = data.channel
                } else if (data.product) {
                    dict.product = data.product
                } else if (data.tag) {
                    dict.tag = [data.tag]
                }
                if (this.href === 'customer') {
                    dict.collection = this.userAuth.collection
                    this.sendSorting('/api/c/sorting', dict)
                }
                if (this.href === 'import') {
                    dict.collection = this.userAuth._import
                    this.sendSorting('/api/m/sorting', dict)
                }
            }
        },
        sendSorting(path, data) {
            this.spinTable = false
            axios.post(path, data)
                .then((res) => {
                    this.spinTable = true
                    this.date = []
                    this.transaction = res.data
                })
                .catch((err) => {
                    this.spinTable = true
                    this.date = []
                    console.error(err)
                })
        },

        //Program RE
        async editedItemRE(items) {
            await items.forEach((item) => {
                let _dict = {
                    old_code: item.id,
                    company: item.name,
                    first_name: item.company,
                    telephone: item.tel,
                    mail: item.email,
                    card_id: item.person_id,
                    tax_id: item.tax_id,
                    refcode: item.product,
                    remark2: item.other,
                    remark1: item.message,
                    cm_call_in: item.channel,
                    line_token: item.userId
                }
                _dict.cm_call_in = _dict.cm_call_in.charAt(0).toUpperCase() + _dict.cm_call_in.substring(1);
                if (!_dict.card_id) {
                    _dict.card_id = ''
                }
                if (!_dict.tax_id) {
                    _dict.tax_id = ''
                }
                if (!_dict.line_token) {
                    _dict.line_token = ''
                }
                if (!_dict.remark2) {
                    _dict.remark2 = ''
                }
                if (_dict.cm_call_in === 'GetDemo' || _dict.cm_call_in === 'Contact' || _dict.cm_call_in === 'Website') {
                    _dict.cm_call_in = '006'
                } else if (_dict.cm_call_in === 'Facebook') {
                    _dict.cm_call_in = '005'
                } else if (_dict.cm_call_in === 'LINE' || _dict.cm_call_in === 'Line' || _dict.cm_call_in === 'Line@') {
                    _dict.cm_call_in = '008'
                }
                this.itemsRE.push(_dict)
            })
            console.log(this.itemsRE)
        },
        async getUserRE() {
            await axios.get('/requests/token/account')
                .then((res) => {
                    this.accountRE = res.data
                })
                .catch((err) => {
                    console.error(err)
                })
        },
        async requestTokenRE() {
            const path = `https://poc.mangoanywhere.com/demosql.sale.re/api/public/RequestApiToken`
            await axios.post(path, this.accountRE)
                .then((res) => {
                    this.tokenRE = res.data.data.token
                })
                .catch((err) => {
                    console.error(err)
                })
        },
        async checkTokenRE(selected) {
            const path = `https://poc.mangoanywhere.com/demosql.sale.re/api/public/CheckToken`
            await axios.get(path, {
                headers: {
                    'x-mg-api-token': this.tokenRE
                }
            })
                .then((res) => {
                    if (res.data.success) {
                        this.$nextTick(() => {
                            this.transaction = selected
                            this.editedItemRE(this.transaction)
                            this.validItemRE()
                        })
                    } else if (!res.data.success) {
                        this.spinRE = true
                        console.log('not valid')
                    }
                })
        },
        async validItemRE() {
            const path = `https://poc.mangoanywhere.com/demosql.sale.re/Re_Api/CustomerValidation?servicetype=MKT`
            await axios.post(path, this.itemsRE, {
                headers: {
                    'x-mg-api-token': this.tokenRE
                }
            })
                .then((res) => {
                    if (res.data.success) {
                        this.spinRE = true
                        this.btnRE = true
                        this.btnAPI = false
                        this.btnHiddenAPI = false
                        this.btnDelete = false
                        this.transaction.forEach((val) => {
                            let idx = this.transaction.indexOf(val)
                            let responseData = res.data.data[idx]
                            let itemsRE = this.itemsRE[idx]
                            if (responseData.customer_code) {
                                Object.assign(val.tag = [responseData.customer_code], val)
                                if (itemsRE.old_code === responseData.id) {
                                    itemsRE.customer_code = responseData.customer_code
                                }
                            } else if (!responseData.customer_code) {
                                Object.assign(val.tag = ['ไม่มีใน RE'], val)
                                if (itemsRE.old_code === responseData.id) {
                                    itemsRE.customer_code = ""
                                }
                            }
                        })
                        this.page = 2
                        this.snackbar = true
                        this.text = `รายการทั้งหมด ${this.transaction.length} รายการ`
                        this.colorSb = 'primary'
                        this.selected = []
                    } else if (!res.data.success) {
                        this.snackbar = true
                        this.text = `มีข้อมูลบางอย่างผิดพลาด กรุณาตรวจสอบข้อมูลก่อน RE`
                        this.colorSb = 'red'
                        console.log(res.data)
                    }
                })
                .catch((err) => {
                    console.error(err)
                })
        },
        closeDuplicateRE() {
            this.dialogDuplicateRE = false
            this.$nextTick(() => {
                this.usersRE = []
                this.itemsDuplicateRE = []
            })
        },
        closeConfirmRE() {
            this.dialogConfirmRE = false
            this.$nextTick(() => {
                this.usersRE = []
                this.itemsDuplicateRE = []
            })
        },
        closeUpdateRE() {
            this.dialogUpdateRE = false
            this.$nextTick(() => {
                this.usersRE = []
                this.itemsDuplicateRE = []
            })
        },
        async editRE() {
            this.usersRE = []
            await this.selected.forEach((item) => {
                let idx = this.transaction.indexOf(item)
                let itemsRE = this.itemsRE[idx]
                if (itemsRE.customer_code) {
                    this.usersRE.push(itemsRE)
                    this.dialogUpdateRE = true
                }
            })
        },
        async finallyEditRE() {
            this.spinButton = false
            const path = 'https://poc.mangoanywhere.com/demosql.sale.re/Re_Api/CustomerUpdate?servicetype=MKT'
            await axios.post(path, this.usersRE, {
                headers: {
                    'x-mg-api-token': this.tokenRE
                }
            })
                .then((res) => {
                    console.log(res.data)
                    if (res.data.success) {
                        this.spinButton = true
                        this.itemsRE = []
                        this.usersRE = []
                        this.itemsDuplicateRE = []
                        this.selected = []
                        this.dialogUpdateRE = false
                        this.initialize().then(() => {
                            this.page = 0
                        })
                        this.text = `คุณได้ทำการอัพเดทรายชื่อใน RE แล้ว!`
                        this.colorSb = 'success'
                        this.snackbar = true
                    } else if (!res.data.success) {
                        this.spinButton = true
                        this.dialogUpdateRE = false
                        this.text = `มีบางอย่างผิดพลาดโปรดตรวจสอบข้อมูลหรือลองใหม่อีกครั้ง!`
                        this.colorSb = 'red'
                        this.snackbar = true
                    }
                })
                .catch((err) => {
                    this.spinButton = true
                    console.error(err)
                })
        },
        createRE() {
            if (this.selected.length === 0) {
                this.text = `กรุณาเลือกข้อมูลก่อนทำรายการ!`
                this.colorSb = 'red'
                this.snackbar = true
            } else {
                this.usersRE = []
                this.selected.forEach((item) => {
                    let idx = this.transaction.indexOf(item)
                    let itemsRE = this.itemsRE[idx]
                    if (itemsRE.customer_code) {
                        this.itemsDuplicateRE.push({
                            id: itemsRE.old_code,
                            customer_code: itemsRE.customer_code,
                            name: itemsRE.company
                        })
                    } else {
                        itemsRE.legal_person = 'N'
                    }
                    this.usersRE.push(itemsRE)
                })
                if (this.itemsDuplicateRE.length > 0) {
                    this.dialogDuplicateRE = true
                } else {
                    this.dialogConfirmRE = true
                }
            }
        },
        async finallyCreate() {
            this.spinButton = false
            const path = `https://poc.mangoanywhere.com/demosql.sale.re/Re_Api/CustomerCreate?servicetype=MKT`
            await axios.post(path, this.usersRE, {
                headers: {
                    'x-mg-api-token': this.tokenRE
                }
            })
                .then((res) => {
                    console.log(res.data)
                    if (res.data.success) {
                        this.selected.forEach((val) => {
                            let idx = this.selected.indexOf(val)
                            let item = res.data.data[idx]
                            if (item.old_code === val.id) {
                                val.tag = [item.customer_code]
                                let data = Object.assign(this.selected[idx], val)
                                this.editTransaction(data, data.id);
                                console.log(data)
                            }
                        })
                        this.spinButton = true
                        this.dialogDuplicateRE = false
                        this.dialogConfirmRE = false
                        this.itemsDuplicateRE = []
                        this.itemsRE = []
                        this.usersRE = []
                        this.initialize().then(() => {
                            this.page = 0
                        })
                        this.text = `คุณได้ทำการเพิ่มข้อมูลไปยังโปรแกรม RE แล้ว!`
                        this.colorSb = 'success'
                        this.snackbar = true
                    } else if (!res.data.success) {
                        this.spinButton = true
                        this.dialogDuplicateRE = false
                        this.dialogConfirmRE = false
                        this.text = `มีบางอย่างผิดพลาดโปรดตรวจสอบข้อมูลหรือลองใหม่อีกครั้ง!`
                        this.colorSb = 'red'
                        this.snackbar = true
                    }
                    console.log(res.data)
                })
                .catch((err) => {
                    this.spinButton = true
                    console.error(err)
                })
        },
        async validCheckRE(selected) {
            if (this.selected.length === 0) {
                this.snackbar = true
                this.text = `กรุณาเลือกข้อมูลเพื่อนำเข้า RE`
                this.colorSb = 'red'
            } else {
                this.spinRE = false
                this.requestTokenRE().then(() => {
                    this.checkTokenRE(selected);
                })

            }
        },
        async moveImport() {
            if (this.selected.length > 0) {
                this.spinImport = true
                const path = '/api/move/customer'
                this.selected.forEach((data) => {
                    data.username = this.userAuth.name
                    data.uid = this.userAuth.uid
                    this.transaction.splice(this.transaction.indexOf(data), 1)
                })
                let dict = {}
                dict.selected = this.selected
                dict.collection = this.userAuth.collection
                dict._import = this.userAuth._import
                await axios.post(path, dict)
                    .then(() => {
                        this.spinImport = false
                        this.text = `คุณได้ทำการย้ายข้อมูลไปหน้า customers แล้ว!`
                        this.colorSb = 'success'
                        this.snackbar = true
                        this.selected = []
                    })
                    .catch((err) => {
                        console.error(err)
                        this.text = 'เกิดข้อผิดพลาด'
                        this.selected = []
                    })
            } else {
                this.colorSb = 'error'
                this.text = 'กรุณาเลือกข้อมูลที่จะต้องทำการย้าย!'
                this.snackbar = true

            }
        },
        async changeTransaction(data) {
            if (data === 'imports') {
                await this.APIImport()
                this.itemsRE = []
                this.selected = []
                this.model = []
            } else if (data === 'customers') {
                await this.initialize()
                this.itemsRE = []
                this.selected = []
                this.model = []
            } else if (data === 'api') {
                this.btnAPI = false
                this.btnHiddenAPI = false
                this.btnImport = false
                this.transaction = []
                this.selected = []
                this.model = []
            }
        },
        sendDeleteMultiple() {
            let dict = {}
            dict.selected = this.selected
            if (this.href === 'customer') {
                dict.collection = this.userAuth.collection
                this.deleteMultiple('/api/customer/delete/multiple', dict)
            } else if (this.href === 'import') {
                dict.collection = this.userAuth._import
                this.deleteMultiple('/api/import/delete/multiple', dict)
            }
        },
        deleteMultiple(path, selected) {
            this.spinDelete = false
            axios.post(path, selected)
                .then((res) => {
                    this.selected.forEach((data) => {
                        this.transaction.splice(this.transaction.indexOf(data), 1)
                    })
                    this.spinDelete = true
                    this.selected = []
                    console.log(res.data)
                })
                .catch((err) => {
                    this.spinDelete = true
                    this.selected = []
                    console.error(err)
                })
        },
        colorProduct(product) {
            if (product === 'Construction') {
                return 'green accent-1'
            }
            if (product === 'RealEstate') {
                return 'blue lighten-4'
            }
            if (product === 'Project Planning') {
                return 'pink lighten-4'
            }
            if (product === 'Consulting') {
                return 'yellow lighten-4'
            }
        },
        async addTransaction(data) {
            let href = this.href
            if (href === 'customer')
                data.collection = this.userAuth.collection
            this.path = '/api/customer'
            if (href === 'import')
                data.collection = this.userAuth._import
            this.path = '/api/import'
            data.uid = this.userAuth.uid
            data.username = this.userAuth.name
            await axios.post(this.path, data)
                .then((res) => {
                    this.spinButton = true;
                    this.transaction.unshift(res.data);
                    this.text = `คุณได้เพิ่มข้อมูล ${this.editedItem.name}`
                    this.colorSb = 'success'
                    this.snackbar = true
                })
                .catch((err) => {
                    this.spinButton = true;
                    console.log(err);
                })
        },
        async editTransaction(data, id) {
            let href = this.href
            if (href === 'customer')
                data.collection = this.userAuth.collection
            this.path = `/api/customer/${id}`
            if (href === 'import')
                data.collection = this.userAuth._import
            this.path = `/api/import/${id}`
            if (!data.tag) {
                data.tag = []
            }
            await axios.put(this.path, data)
                .then(() => {
                    this.spinButton = true;
                    this.colorSb = 'primary'
                    this.text = `คุณได้อัพเดทข้อมูล ${this.editedItem.name}`
                    this.snackbar = true
                    this.selected = []
                })
                .catch((err) => {
                    this.spinButton = true;
                    console.log(err);
                })
        }
        ,
        async deleteTransaction(id) {
            let href = this.href
            if (href === 'customer')
                this.path = `/api/customer/${id}?collection=${this.userAuth.collection}`
            if (href === 'import')
                this.path = `/api/import/${id}?collection=${this.userAuth._import}`
            await axios.delete(this.path)
                .then(() => {
                    this.selected = []
                    this.spinButton = true;
                    this.colorSb = 'red'
                    this.text = `คุณได้ลบข้อมูล ${this.editedItem.name}`
                    this.snackbar = true
                })
                .catch((err) => {
                    this.spinButton = true;
                    console.log(err);
                })
        },
        editItem(item) {
            this.editedIndex = this.transaction.indexOf(item)
            this.editedItem = Object.assign({}, item)
            this.dialogCustomer = true;
        },
        deleteItem(item) {
            this.editedIndex = this.transaction.indexOf(item)
            this.editedItem = Object.assign({}, item)
            this.dialogDelete = true
        },
        async deleteItemConfirm() {
            this.spinButton = false;
            await this.deleteTransaction(this.editedItem.id);
            this.transaction.splice(this.editedIndex, 1);
            this.closeDelete()
        },
        close() {
            this.dialogCustomer = false
            this.$nextTick(() => {
                this.editedItem = Object.assign({}, this.defaultItem)
                this.editedIndex = -1
            })
        },
        closeDelete() {
            this.dialogDelete = false
            this.$nextTick(() => {
                this.editedItem = Object.assign({}, this.defaultItem)
                this.editedIndex = -1
            })
        },
        async save() {
            if (this.editedIndex > -1) {
                this.spinButton = false;
                let data = Object.assign(this.transaction[this.editedIndex], this.editedItem);
                await this.editTransaction(data, data.id);
            } else {
                this.spinButton = false;
                await this.addTransaction(this.editedItem);
            }
            this.close()
        },

        // tags
        async getTags() {
            const path = `/api/tag?collection=tags_${this.userAuth.collection}`
            await axios.get(path)
                .then((res) => {
                    this.itemsTag = res.data
                })
                .catch((err) => {
                    console.error(err)
                })
        },
        filter(item, queryText, itemText) {
            const hasValue = val => val != null ? val : ''
            const text = hasValue(itemText)
            const query = hasValue(queryText)
            return text.toString()
                .toLowerCase()
                .indexOf(query.toString().toLowerCase()) > -1
        },
        edit(index, item) {
            if (!this.editingTag) {
                this.editingTag = item
                this.editingIndexTag = index

            } else {
                this.setTag(item.id, this.editingTag)
                this.editingTag = null
                this.editingIndexTag = -1
            }
        },
        addTag(item) {
            const path = `/api/tag/add/new?collection=tags_${this.userAuth.collection}&tag=${item.text}`
            axios.get(path)
                .then(() => {
                    this.getTags()
                    console.log('success')
                })
                .catch((err) => {
                    console.error(err)
                })
        },
        setTag(id, item) {
            const path = `/api/tag/${id}?collection=tags_${this.userAuth.collection}`;
            axios.put(path, item)
                .then(() => {
                    console.log('success')
                })
                .catch((error) => {
                    console.error(error)
                })
        },
        toRemove(index, item) {
            this.itemsTag.splice(this.itemsTag.indexOf(item), 1)
            this.removeTag(item.id)
        },
        removeTag(id) {
            const path = `/api/tag?id-query=${id}&collection=tags_${this.userAuth.collection}`;
            axios.delete(path)
                .then(() => {
                    this.getTags()
                    console.log('success')
                })
                .catch((error) => {
                    console.error(error)
                })
        },
        tagTransaction(selected) {
            this.spinTag = false
            let data = {
                id: selected,
                tag: this.model,
                href: this.href,
                collection: this.userAuth.collection,
                _import: this.userAuth._import
            }
            const path = '/api/tag'
            axios.post(path, data)
                .then((res) => {
                    this.spinTag = true
                    if (this.href === 'customer') {
                        this.initialize()
                    } else if (this.href === 'import') {
                        this.APIImport()
                    }
                })
                .catch((err) => {
                    console.error(err)
                })
        },

        // import Excel
        importExcel() {
            let formData = new FormData();
            formData.append('file', this.fileImportExcel);
            formData.append('uid', this.userAuth.uid);
            formData.append('username', this.userAuth.name);
            this.spinButton = false
            if (this.href === 'customer') {
                formData.append('collection', this.userAuth.collection)
                this.APIImportExcel('/api/customer/import/excel', formData)
            } else if (this.href === 'import') {
                formData.append('collection', this.userAuth._import)
                this.APIImportExcel('/api/import/import/excel', formData)
            }
        },

        async APIImportExcel(path, data) {
            await axios.post(path, data)
                .then(() => {
                    this.spinButton = true
                    this.dialogImportExcel = false
                    this.fileImportExcel = null
                    if (this.href === 'customer') {
                        this.initialize()
                    } else if (this.href === 'import') {
                        this.APIImport()
                    }
                })
                .catch((err) => {
                    console.error(err)
                    this.spinButton = true
                    this.fileImportExcel = null
                    this.snackbar = true
                    this.text = 'มีบางอย่างผิดพลาดอาจเป็น format excel!'
                    this.colorSb = 'red'
                })
        },

        closeImportExcel() {
            this.dialogImportExcel = false
            this.$nextTick(() => {
                this.fileImportExcel = null
            })
        },

        async excelPreview() {
            this.spinPreview = false
            const path = '/api/preview/excel'
            await axios.get(path, {
                headers: {
                    'Content-Type': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
                    'Content-Disposition': "attachment; filename=preview.xlsx"
                },
                responseType: 'blob',
            })
                .then((res) => {
                    console.log(res.data)
                    const blob = res.data;
                    const link = document.createElement("a");

                    link.href = URL.createObjectURL(blob);
                    link.download = 'preview.xlsx';
                    document.body.appendChild(link);
                    link.click();
                    document.body.removeChild(link);
                    this.spinPreview = true
                })
                .catch((err) => {
                    console.error(err)
                    this.snackbar = true
                    this.text = 'มีบางอย่างผิดพลาด ลองใหม่อีกครั้ง'
                    this.colorSb = 'red'
                    this.spinPreview = true
                })
        },

        logout() {
            return window.location = '/secure/logout'
        },

        //appBar
        redirectPage(item) {
            console.log(item)
            if (item.text === 'Mango')
                window.location = '/'
            if (item.text === 'Intents')
                window.location = '/intents'
            if (item.text === 'Dashboard')
                window.location = '/dashboard'
        },

        //copy
        copyTag(data) {
            this.snackbar = true
            this.text = `คัดลอก ${data}`
            this.colorSb = 'primary'
        },

    }
    ,
    delimiters: ["[[", "]]"]
})