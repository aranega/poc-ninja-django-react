/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';
export class DefaultService {
    /**
     * Create Schools
     * @returns any OK
     * @throws ApiError
     */
    public static createSchools(): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/api/generate',
        });
    }
}
