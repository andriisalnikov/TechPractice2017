import { Injectable } from '@angular/core';
import { Http, Response } from '@angular/http';
import { Observable } from 'rxjs/Observable';
import { Competition } from './app.competition';
import { UrlHelper } from '../common/UrlHelper';
import 'rxjs/add/operator/catch';
import 'rxjs/add/operator/map';

@Injectable()
export class CompetitionService {
    private heroesUrl = UrlHelper.BaseUrl+"/api/competitions/all";
    private createURL = UrlHelper.BaseUrl+'/api/competitions/create';
    constructor(private http:Http) {
    
    }
    getCategories():Observable<Competition[]>{
         return this.http.get(this.heroesUrl)
                    .map((res:Response)=> res.json() as Competition[])
                    .catch((error:any) => Observable.throw(error.json().error || 'Server error'));
    }
    private extractData(res:Response){
        let body = res.json();
        return body;
    }
    private handleError(error:Response|any){
        return Observable.throw(error);
    }
}