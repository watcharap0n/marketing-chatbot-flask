new Vue({
    el: '#app',
    vuetify: new Vuetify(),
    data: {
        validCheck: [v => !!v || 'กรุณาคลิกเพื่อไปต่อ'],
        validSelect: [v => !!v || 'กรุณาเลือกผลิตภัณฑ์'],
        validEmail: [
            v => !!v || 'กรุณากรอกอีเมล',
            v => /.+@.+\..+/.test(v) || 'กรุณากรอกอีเมลให้ถูกต้อง',
        ],
        validTel: [
            v => !!v || 'กรุณากรอกเบอร์โทร',
            v => (v && v.length <= 10) || 'เบอร์โทรกรอกไม่ครบ',
        ],
        validOther: [v => !!v || 'กรุณากรอกข้อมูลให้ครบถ้วน'],
        formElement: {
            name: '',
            email: '',
            company: '',
            tel: '',
            product: '',
            other: '',
            message: '',
            userId: '',
            email_private: '',
            profile: '',
            picture: '',
            collection: '',
        },
        form: {},
        valid: false,
        spinBtn: true,
        spinPage: false,
    },
    delimiters: ["[[", "]]"],
    async mounted() {
        this.form.id = this.$refs.formId.value
        await this.getForm()
        await liff.init({liffId: this.form.token_liff}, () => {
                if (liff.isLoggedIn()) {
                    this.spinPage = true
                    liff.getProfile()
                        .then((profile) => {
                            console.log(liff.getContext());
                            this.formElement.userId = profile.userId
                            this.formElement.profile = profile.displayName
                            this.formElement.picture = profile.pictureUrl
                            this.formElement.email_private = liff.getDecodedIDToken().email
                        })
                } else {
                    this.spinPage = true
                    liff.login();
                }
            }
        )
    },
    methods: {
        async getForm() {
            const path = `/api/form/custom/get?id=${this.form.id}`
            await axios.get(path)
                .then((res) => {
                    this.form = res.data.item
                    this.spinData = true
                })
                .catch((err) => {
                    console.error(err);
                })
        },
        onSubmit() {
            let validate = this.$refs.form.validate()
            if (validate === true) {
                this.spinBtn = false
                const path = `/api/all/questionnaire?collection=${this.formElement.collection}`
                this.formElement.channel = this.form.channel
                axios.post(path, this.formElement)
                    .then(() => {
                        this.spinBtn = true
                        this.popUp()
                        this.$refs.form.reset()
                    })
                    .catch((err) => {
                        this.spinBtn = true
                        Swal.fire("มีบางอย่างผิดพลาด", "กรุณาลองใหม่อีกครั้งค่ะ", "error").then(() => {
                            liff.closeWindow();
                        })
                    })
            }
        },
        popUp() {
            Swal.fire("ข้อมูลบันทึกเรียบร้อย!", "เจ้าหน้าที่ได้รับข้อมูลของท่านแล้ว\nและจะดำเนินการติดต่อกลับให้เร็วที่สุด", "success").then(() => {
                liff.closeWindow();
            })
        },
    }
})