Page({
  form1Submit(e) {
    wx.request({
      url: "https://www.example.com/form",
      method: 'POST',
      data: e.detail.value,
      success(res) {
        if (res.statusCode === 200) {
          wx.showToast({
            title: '提交成功',
            icon: 'success'
          });
        } else {
          wx.showToast({
            title: '提交失败',
            icon: 'none'
          });
        }
      },
      fail(err) {
        wx.showToast({
          title: '网络错误',
          icon: 'none'
        });
      }
    });
  },
})