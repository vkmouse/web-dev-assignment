function render() {
  const topics = [{
    id: 'topic-1',
    url: 'https://docs.google.com/presentation/d/e/2PACX-1vRL-RfyaW2zyPo22TBOPhYMr4tdsngn4JE0rzAkvtRyeAEj1PAavYOtM8wOiCF0Z8LAyk6dlOTtsG6D/embed',
    title: '主題一、使用 Grid 完成排版',
    items: [  
      'Grid 至 2017 年被瀏覽器支援',
      'Grid 以面積為概念思考',
      'Grid 思考順序 1. 橫列 2. 直排 3. 排版',
      'Grid 相比於傳統 Div 排版更靈活、容易修改',
    ],
  }, {
    id: 'topic-2',
    url: 'https://docs.google.com/presentation/d/e/2PACX-1vR0WNxJzOsCmMym1mW5PYaxl9KHv0jnjWVA_xW73BcRnc8RjNzcM5EsTUfDOQBeJRYYqgUi7Xj7wpEO/embed',
    title: '主題二、完善資料驗證程序',
    items: [  
      '前端驗證: 移除不需要的請求',
      '1. 增加回應速度',
      '2. 減少後端負荷',
      '',
      '後端驗證: 確認資料合法，才操作資料庫',
      '1. 避免資料庫存取不合法資料',
      '2. 避免不正常使用者操作',
    ],
  }, {
    id: 'topic-3',
    url: 'https://docs.google.com/presentation/d/e/2PACX-1vQTCsfKpRkd8rXwRT21mJr3Fv09jQYssWrMUU-k_EvK4OK3i-BV3ogzFIPcgGVa6RYscz1an7nfdyM4/embed',
    title: '主題三、AJAX 與 CORS',
    items: [  
      '跨來源請求資源時，會有 CORS 進行阻擋',
      'CORS 會造成瀏覽器阻擋 Response',
      '要開放 API 時，需要 access-control-allow-origin 標頭 (* 允許所有 domains)',
    ],
  }]

  for (const topic of topics) {
    const { id, url, title, items } = topic
    const section = document.getElementById(id)
    section.appendChild(createSectionMain(url))
    section.appendChild(createSectionAside(title, items))
  }
}

function createSectionMain(url) {
  const iframe = document.createElement('iframe')
  iframe.className = 'slice ratio'
  iframe.src = url

  const div = document.createElement('div')
  div.className = 'ratio-container'
  div.appendChild(iframe)

  const element = document.createElement('div');
  element.className = 'section-main'
  element.appendChild(div)
  return element
}

function createSectionAside(title, items) {
  const element = document.createElement('div');
  element.className = 'section-aside'
  element.appendChild(createH4(title))
  for (const item of createLines(items)) {
    element.appendChild(item)
  }
  return element
}

function createH4(title) {
  const element = document.createElement('h4');
  element.textContent = title
  return element
}

function createLines(items) {
  const elements = []
  for (const item of items) {
    const element = document.createElement('p');
    element.textContent = item
    elements.push(element)
  }
  return elements
}

render()