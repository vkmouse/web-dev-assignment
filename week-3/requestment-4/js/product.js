class Product {
  dataSource
  subProductController
  mainProductController

  constructor() {
    this.dataSource = new DataSource()
    this.subProductController = new SubProductController()
    this.mainProductController = new MainProductController()

    this.dataSource.dataChangedHandler.push(() =>
      this.subProductController.updateProducts(this.dataSource.dataset))
    this.dataSource.dataChangedHandler.push(() =>
      this.mainProductController.updateProducts(this.dataSource.dataset))
  }

  init() {
    this.dataSource.init()
  }

  loadMore(element) {
    const numData = this.dataSource.dataset.length
    const { start, end } = this.mainProductController
    this.mainProductController.start = Math.min(start + 8, numData)
    this.mainProductController.end = Math.min(end + 8, numData)
    this.mainProductController.updateProducts(this.dataSource.dataset)

    if (this.mainProductController.start === numData) {
      element.style.display = "none";
    }
  }
}

class SubProductController {
  start = 0
  end = 2

  updateProducts(dataset) {
    const subProductContainer = document.getElementById('sub-product-container')
    for (const data of dataset.slice(this.start, this.end)) {
      const node = this.createProduct(data.title, data.url)
      subProductContainer.appendChild(node)
    }
  }

  createProduct(title, url) {
    const product = document.createElement('div');
    product.className = "product sub-product bg-secondary"
    product.appendChild(this.createImg(title, url))
    product.appendChild(this.createTitle(title))
    return product
  }

  createImg(title, url) {
    const productImg = document.createElement('img');
    productImg.className = "sub-product__img center-cropped" 
    productImg.src = url
    productImg.title = title
    productImg.alt = title
    return productImg
  }

  createTitle(title) {
    const productTitle = document.createElement('div');
    productTitle.className = "sub-product__title"
    productTitle.textContent = title
    return productTitle
  }
}

class MainProductController {
  start = 2
  end = 10

  updateProducts(dataset) {
    const mainProductContainer = document.getElementById('main-product-container')
    for (const data of dataset.slice(this.start, this.end)) {
      const node = this.createProduct(data.title, data.url)
      mainProductContainer.appendChild(node)
    }
  }

  createProduct(title, url) {
    const product = document.createElement('div')
    product.appendChild(this.createStar())
    product.appendChild(this.createImg(title, url))
    product.appendChild(this.createTitle(title))
    product.className = 'product main-product ratio-1x1'
    return product
  }

  createStar() {
    const starContainer = document.createElement('div')
    const star = document.createElement('div')
    starContainer.appendChild(star)
    starContainer.className = 'main-product__star-container ratio-element'
    star.className = 'star'
    star.onclick = () => handleStarClick(star)
    return starContainer
  }

  createImg(title, url) {
    const productImg = document.createElement('img')
    productImg.className = 'main-product__img ratio-element center-cropped'
    productImg.src = url
    productImg.title = title
    productImg.alt = title
    return productImg
  }

  createTitle(title) {
    const wrapper = document.createElement('div')
    const productTitleContainer = document.createElement('div')
    const productTitle = document.createElement('div')
    wrapper.append(productTitleContainer)
    productTitleContainer.append(productTitle)
    productTitleContainer.append(this.createToolTip(title))
    productTitleContainer.append(this.createOverlay())
    wrapper.className = 'ratio-element d-flex'
    productTitleContainer.className = 'main-product__title-container'
    productTitle.className = 'main-product__title'
    productTitle.textContent = title
    return wrapper
  }

  createToolTip(title) {
    const tooltip = document.createElement('div')
    tooltip.className = 'main-product__tooltip'
    tooltip.textContent = title
    return tooltip
  }
  
  createOverlay() {
    const overlay = document.createElement('div')
    overlay.className = 'main-product__overlay'
    return overlay
  }
}