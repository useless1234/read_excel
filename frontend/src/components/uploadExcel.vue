<template>
  <el-upload
    class="upload-demo"
    ref="upload"
    action="123"
    :before-upload="beforeUpload"
    :on-preview="handlePreview"
    :on-remove="handleRemove"
    :file-list="fileList"
    :auto-upload="false">
    <el-button slot="trigger" size="small" type="primary">选取文件</el-button>
    <el-button style="margin-left: 10px;" size="small" type="success" @click="submitUpload">上传到服务器</el-button>
    <div slot="tip" class="el-upload__tip">只能上传jpg/png文件，且不超过500kb</div>
  </el-upload>
</template>

<script>
  export default {
    name: "uploadExcel",
    data() {
      return {
        fileList: []
      };
    },
    methods:{
      submitUpload() {
        this.$refs.upload.submit();
      },
      handleRemove(file, fileList) {
        console.log(file, fileList);
      },
      handlePreview(file) {
        console.log(file);
      },
      beforeUpload(file){
        console.log(file);
        let fd = new FormData();
        fd.append("file", file);
        this.$axios.post('upload_file', fd).then(res => {
            console.log('success')
        })
      }
    }
  }
</script>

<style scoped>

</style>
