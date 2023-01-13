import { request } from '@/api/service'

export const urlPrefix = '/api/project/online_version/'

export function getFileData () {
  return request({
    url: urlPrefix,
    method: 'get'
  })
}

export function selectVersionNumber (yearMonth) {
  return request({
    url: urlPrefix + 'select_version_number/',
    data: { yearMonth },
    method: 'post'
  })
}

export function searchByOnlineVersion (obj) {
  return request({
    url: urlPrefix + 'search_by_online_version/',
    data: obj,
    method: 'post'
  })
}
