class DataSource {
  dataChangedHandler = []
  dataset = []

  init() {
    const url = 'https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json'
    fetch(url)
      .then(response => response.json())
      .then(response => {
        this.dataset = response['result']['results'].map(p => this.convertToData(p))
        for (const onDataChanged of this.dataChangedHandler) {
          onDataChanged()
        }
    })
  }

  convertToData(result) {
    return {
      title: result['stitle'],
      url: 'https' + result['file'].split('https').slice(1)[0]
    }
  }
}